import pandas as pd
import ast

def safe_literal_eval(val):
    """
    安全地将字符串转换为原始格式（列表或字典），对于无效格式返回原始值。
    """
    try:
        return ast.literal_eval(val) if not pd.isna(val) else val
    except (ValueError, SyntaxError):
        return val
