# Zimi: 汉字字形谜解谜模型

Zimi 项目旨在开发和实现一个基于深度学习的汉字字形谜自动解答系统。该系统利用预训练语言模型，通过结构预测、关键词提取和谜底映射等多个模块，解决汉字字形谜的结构解析和谜底生成问题。

## 项目结构

```plaintext
zimi/
    generate_tree.py                 # 生成文件夹树状结构的脚本
    directory_structure.txt          # 文件夹树状结构输出
    main.py                          # 主程序文件，整合模型，进行预测
    data/
        processed/
            zimi/
                processed_chinese.csv  # 处理后的汉字数据
                chinese.csv            # 初步处理后的汉字数据
        results/
            mapping_dict.json          # 结构和拆字谜底到字符的映射字典
            index_to_label.json        # 结构谜底索引到标签的映射
            label_to_index.json        # 结构谜底标签到索引的映射
            zimi_result_data.csv       # 预测结果文件
        raw/
            chinese_character/
                char_common_detail.json # 汉字详细信息数据
                char_common_base.json   # 汉字基本信息数据
                chaizi.txt              # 拆字数据
                hanzi_structure.csv     # 汉字结构方式数据
        riddles/
            zimi/
                zimi_task_data.csv      # 测试集字谜数据
                zimi_train_data.csv     # 训练集字谜数据
    hanzi_riddles/
        utils.py                       # 工具函数
        config.py                      # 配置文件
        riddle_generation.py           # 字谜生成相关代码
        __init__.py                    # 包初始化
        riddle_templates.py            # 字谜模板
        README.md                      # 说明文档
        __pycache__/                   # Python 缓存文件
    hanzi_processing/
        utils.py                       # 工具函数
        config.py                      # 配置文件
        __init__.py                    # 包初始化
        hanzi_structure.py             # 汉字结构处理
        README.md                      # 说明文档
        data_preparation.py            # 数据准备相关代码
        __pycache__/                   # Python 缓存文件
    models/
        keyword_extractor/             # 关键词提取模型相关文件
            tokenizer_config.json
            vocab.txt
            model.safetensors
            special_tokens_map.json
            generation_config.json
            config.json
        structure_classifier/          # 结构分类器模型
            riddle_classifier.pth
    train/
        structure_model.ipynb          # 结构分类模型训练 Notebook
        key_word_model.ipynb           # 关键词提取模型训练 Notebook
    scripts/
        generate_riddles.py            # 字谜生成脚本
        process_hanzi_data.py          # 汉字数据处理脚本
```

## 安装

1. **克隆代码库**：
   ```bash
   git clone https://github.com/MarrytheToilet/zimi
   cd zimi
   ```

2. **创建虚拟环境并激活**：
   ```bash
   # 使用 Anaconda
   conda create --name llm_env python=3.9
   conda activate llm_env
   ```

3. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 数据处理

使用 `process_hanzi_data.py` 处理原始汉字数据：

```bash
python scripts/process_hanzi_data.py
```

### 字谜生成

使用 `generate_riddles.py` 生成字谜：

```bash
python scripts/generate_riddles.py
```

### 训练模型

模型的训练过程在 `train/` 文件夹下包含两个 Jupyter Notebook：

- `structure_model.ipynb`：训练汉字字形结构分类模型
- `key_word_model.ipynb`：训练关键词提取模型

打开这些 Notebook 并按照其中的步骤运行代码以训练模型。注意：在使用 Jupyter Notebook 训练模型时，请注意模型保存路径。确保将训练好的模型保存到` models/` 目录，并更新路径配置。

### 运行主程序

使用 `main.py` 进行字谜的解谜预测：

```bash
python main.py
```

## 目录说明

- **data/**: 包含原始、处理后的数据，以及字谜生成的数据。
- **hanzi_processing/**: 包含汉字数据处理相关的代码。
- **hanzi_riddles/**: 包含字谜生成和处理相关的代码。
- **models/**: 存放训练好的模型文件。
- **train/**: 包含训练模型的 Jupyter Notebook。
- **scripts/**: 包含数据处理和字谜生成的脚本。
- **main.py**: 主程序文件，用于运行整个解谜过程。


### 使用说明

- **安装依赖**：确保在虚拟环境中运行并安装所需的 Python 库。
- **处理数据**：执行数据处理脚本来生成所需的数据文件。
- **生成字谜**：运行字谜生成脚本以生成训练和测试数据。
- **训练模型**：使用 Notebook 训练模型，并将训练好的模型保存到 `models/` 目录。
- **运行预测**：使用 `main.py` 运行字谜的解谜预测。
