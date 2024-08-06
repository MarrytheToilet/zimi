import random

def create_riddle(row, riddle_template):
    """
    基于模板生成字谜。
    """
    first_element = row['拆字'][0] if row['拆字'] and len(row['拆字']) > 0 else ""

    elements = first_element.split()

    # 根据结构代码选择合适的模板并生成谜语
    structure_code = row['结构代码'][0]

    if structure_code in riddle_template:
        # 处理上下（B）和左右（H）以及全包围（Q）结构的情况
        if structure_code in ['B', 'H', 'Q'] and len(elements) == 2:
            template = random.choice(riddle_template[structure_code])
            return template.format(elements[0], elements[1])
        # 处理上中下（E）结构和左中右（M）结构的情况
        elif structure_code in ['E', 'M'] and len(elements) == 3:
            template = random.choice(riddle_template[structure_code])
            return template.format(elements[0], elements[1], elements[2])
    return None
