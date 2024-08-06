import pandas as pd
import ast
import json
from sentence_transformers import SentenceTransformer
from transformers import BertTokenizer, BartForConditionalGeneration, Text2TextGenerationPipeline
import torch
import torch.nn as nn
from tqdm import tqdm

# 配置路径
processed_data_path = "./data/riddles/zimi/zimi_task_data.csv"
mapping_dict_path = "./data/results/mapping_dict.json"
index_to_label_path = "./data/results/index_to_label.json"
label_to_index_path = "./data/results/label_to_index.json"
structure_classifier_model_path = "./models/structure_classifier/riddle_classifier.pth"
keyword_extractor_model_path = "./models/keyword_extractor"

# embedding_model_path = "BAAI/bge-small-zh-v1.5"
embedding_model_path = "BAAI/bge-small-zh-v1.5"

# 转换拆字列和pronunciation_details列
def safe_literal_eval(val):
    try:
        return ast.literal_eval(val) if not pd.isna(val) else val
    except (ValueError, SyntaxError):
        return val

# 加载资源
def load_resources():
    with open(mapping_dict_path, 'r', encoding='utf-8') as f:
        mapping_dict = json.load(f)

    with open(index_to_label_path, 'r', encoding='utf-8') as f:
        index_to_label = {int(k): v for k, v in json.load(f).items()}

    with open(label_to_index_path, 'r', encoding='utf-8') as f:
        label_to_index = json.load(f)

    sentence_model = SentenceTransformer(embedding_model_path).to('cuda')
    classifier_model = RiddleStructureClassifier(sentence_model, len(label_to_index)).to('cuda')
    classifier_model.load_state_dict(torch.load(structure_classifier_model_path))
    classifier_model.eval()

    tokenizer = BertTokenizer.from_pretrained(keyword_extractor_model_path)
    keyword_model = BartForConditionalGeneration.from_pretrained(keyword_extractor_model_path).eval()
    
    return classifier_model, keyword_model, tokenizer, mapping_dict, index_to_label

# 定义分类器
class RiddleStructureClassifier(nn.Module):
    def __init__(self, embedding_model, num_labels):
        super(RiddleStructureClassifier, self).__init__()
        self.embedding_model = embedding_model
        self.dropout = nn.Dropout(0.3)
        self.classifier1 = nn.Linear(embedding_model.get_sentence_embedding_dimension(), 768)
        self.classifier2 = nn.Linear(768, num_labels)

    def forward(self, input_sentences):
        embeddings = self.embedding_model.encode(input_sentences, convert_to_tensor=True).to('cuda')
        x_1 = self.dropout(embeddings)
        x_2 = nn.ReLU()(self.classifier1(x_1))
        logits = self.classifier2(x_2)
        return logits
    
    def classify(self, riddles, index_to_label):
        self.eval()
        with torch.no_grad():
            logits = self(riddles)
            _, predicted_indices = torch.max(logits, 1)
            predicted_labels = [index_to_label[idx.item()] for idx in predicted_indices]
            return predicted_labels

# 测试字谜
def test_riddle(riddle, classifier, text2text_generator, mapping_dict, index_to_label):
    predicted_structure = classifier.classify([riddle], index_to_label)[0]
    input_text = f"请抽取字谜中的关键字：{riddle}。字谜中的关键字是：[MASK]"

    generation = text2text_generator(input_text, max_length=10, do_sample=False)
    predicted_keyword = generation[0]['generated_text'].replace(" ", "")
    predicted_answer = mapping_dict.get(predicted_structure + predicted_keyword, "未找到匹配的谜底")

    return predicted_structure, predicted_keyword, predicted_answer

# 主函数
def main():
    zimi_df = pd.read_csv(processed_data_path).dropna()
    zimi_df['拆字'] = zimi_df['拆字'].apply(safe_literal_eval)
    zimi_df['pronunciation_details'] = zimi_df['pronunciation_details'].apply(safe_literal_eval)
    zimi_df = zimi_df[['字符', '结构代码', '结构方式', '间架比例', '字谜', '结构谜底', '拆字谜底', '谜底']]

    classifier, keyword_model, tokenizer, mapping_dict, index_to_label = load_resources()
    text2text_generator = Text2TextGenerationPipeline(keyword_model, tokenizer)

    data = zimi_df.copy()
    data['预测结构'] = pd.Series(dtype='str')
    data['预测拆字'] = pd.Series(dtype='str')
    data['预测谜底'] = pd.Series(dtype='str')
    data['预测字符'] = pd.Series(dtype='str')

    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        riddle = row['字谜']
        predicted_structure, predicted_keyword, predicted_answer = test_riddle(riddle, classifier, text2text_generator, mapping_dict, index_to_label)

        data.at[index, '预测结构'] = predicted_structure
        data.at[index, '预测拆字'] = predicted_keyword
        data.at[index, '预测谜底'] = predicted_structure + predicted_keyword
        data.at[index, '预测字符'] = predicted_answer

    correct_structures = (data['结构谜底'] == data['预测结构']).sum()
    correct_keyword = (data['拆字谜底'] == data['预测拆字']).sum()
    correct_answers = (data['谜底'] == data['预测谜底']).sum()
    correct_character = (data['字符'] == data['预测字符']).sum()
    total = len(data)

    print(f"结构谜底正确率: {correct_structures/total*100:.2f}%")
    print(f"拆字谜底正确率: {correct_keyword/total*100:.2f}%")
    print(f"谜底正确率: {correct_answers/total*100:.2f}%")
    print(f"字符正确率: {correct_character/total*100:.2f}%")

    data.to_csv("./data/results/zimi_result_data.csv")

if __name__ == '__main__':
    main()
