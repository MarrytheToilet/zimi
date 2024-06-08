import pandas as pd
import json
from hanzi_processing.utils import safe_literal_eval

def read_chaizi_file(file_path):
    """
    读取并处理 chaizi.txt 文件，返回汉字和其拆分部件的字典。
    """
    chaizi_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            char = parts[0]
            components = parts[1:]
            chaizi_dict[char] = components
    return chaizi_dict

def read_json_lines(file_path):
    """
    逐行读取 JSON 文件，返回解析后的列表。
    """
    json_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                json_obj = json.loads(line.strip(',\n'))
                json_list.append(json_obj)
            except json.JSONDecodeError as e:
                print(f"Error parsing line: {line}. Error: {e}")
    return json_list

def load_and_process_data(file_path):
    """
    加载并处理汉字数据文件。
    """
    df = pd.read_csv(file_path).dropna()
    df['拆字'] = df['拆字'].apply(safe_literal_eval)
    df['pronunciation_details'] = df['pronunciation_details'].apply(safe_literal_eval)
    return df

def filter_data(df):
    """
    筛选符合条件的数据。
    """
    df_filtered = df[(df['笔画数'] >= 3) & (df['笔画数'] <= 10)]
    df_filtered = df_filtered[df_filtered['结构代码'].str.startswith(('B', 'H'))]
    return df_filtered

def create_structure_answer(row):
    """
    生成结构谜底。
    """
    structure = "上下" if row['结构代码'].startswith('B') else "左右" if row['结构代码'].startswith('H') else ""
    return f"[{structure}]" if structure else None

def create_chaizi_answer(row):
    """
    生成拆字谜底。
    """
    chaizi = row['拆字'][0].replace(" ","") if row['拆字'] and len(row['拆字']) > 0 else ""
    return chaizi if chaizi else None

def add_answers(df):
    """
    添加结构谜底和拆字谜底。
    """
    df['结构谜底'] = df.apply(create_structure_answer, axis=1)
    df['拆字谜底'] = df.apply(create_chaizi_answer, axis=1)
    df['谜底'] = df['结构谜底'] + df['拆字谜底']
    return df.dropna()

def create_riddle_mapping(df):
    """
    创建谜底和字符的映射字典。
    """
    mapping_dict = {}
    for index, row in df.iterrows():
        answer = row['谜底']
        character = row['字符']
        if pd.notnull(answer) and pd.notnull(character) and answer not in mapping_dict:
            mapping_dict[answer] = character
    return mapping_dict
