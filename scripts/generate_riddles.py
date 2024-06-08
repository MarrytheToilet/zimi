import pandas as pd
from sklearn.model_selection import train_test_split
from hanzi_riddles.riddle_generation import create_riddle
from hanzi_riddles.riddle_templates import riddle_templates
import hanzi_riddles.config as config
from hanzi_riddles.utils import safe_literal_eval

def main():
    # 加载处理后的数据
    data = pd.read_csv(config.chinese_data_output_path)

    data['拆字'] = data['拆字'].apply(safe_literal_eval)
    data['pronunciation_details'] = data['pronunciation_details'].apply(safe_literal_eval)      
    
    # 数据集划分为训练集和测试集
    train_df, test_df = train_test_split(data, test_size=0.3, random_state=42)

    # 生成训练集字谜
    train_df['字谜'] = train_df.apply(lambda row: create_riddle(row, riddle_template=riddle_templates['train']), axis=1)
    train_df.dropna().to_csv(config.train_data_path, index=False)
    print("训练数据已保存到:", config.train_data_path)

    # 生成测试集字谜
    test_df['字谜'] = test_df.apply(lambda row: create_riddle(row, riddle_template=riddle_templates['test']), axis=1)
    test_df.dropna().to_csv(config.test_data_path, index=False)
    print("测试数据已保存到:", config.test_data_path)

if __name__ == '__main__':
    main()
