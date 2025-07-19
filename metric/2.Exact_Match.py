import token
import tokenize
from io import StringIO
from utils.get_keywords_ops_com_ter import get_keywords_ops_comment

def remove_comment(code_str,language):
    lines=code_str.split("\n")
    _, _, comment,_=get_keywords_ops_comment(language)
    cleaned_line=[]
    for line in lines:
        if line[0:2]!=comment:
            cleaned_line.append(line)
    return cleaned_line



