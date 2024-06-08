import random

def create_riddle(row, riddle_template):
    """
    基于模板生成字谜。
    """
    first_element = row['拆字'][0] if row['拆字'] and len(row['拆字']) > 0 else ""

    elements = first_element.split()

    if len(elements) == 2:
        if row['结构代码'][0] in riddle_template:
            template = random.choice(riddle_template[row['结构代码'][0]])
            return template.format(elements[0], elements[1])
    return None
