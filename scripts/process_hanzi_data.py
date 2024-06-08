import pandas as pd
from hanzi_processing.data_preparation import load_and_process_data, filter_data, add_answers, create_riddle_mapping
import hanzi_processing.config as config
import json

def main():
    # 加载并处理数据
    data = load_and_process_data(config.chinese_data_path)
    data_filtered = filter_data(data)
    data_with_answers = add_answers(data_filtered)

    # 创建映射字典并保存
    mapping_dict = create_riddle_mapping(data_with_answers)
    with open(config.mapping_dict_path, 'w', encoding='utf-8') as f:
        json.dump(mapping_dict, f, ensure_ascii=False, indent=4)
    print("映射字典已保存到:", config.mapping_dict_path)

    # 保存处理后的数据
    data_with_answers.to_csv(config.chinese_data_output_path, index=False)
    print("处理后的数据已保存到:", config.chinese_data_output_path)

if __name__ == '__main__':
    main()
