import re
import os


def my_open_file(path):
    file = open(path,"r", encoding="utf-8")
    result = []
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        result.append(line)
    file.close()
    return result


def my_open_file_content(path):
    file = open(path, "r", encoding="utf-8")
    result = ""
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        result = result + line + " "
    file.close()
    return result


def my_write_file(path, content):
    file = open(path, "w", encoding="utf-8")
    file.write(content)
    file.close()


def my_str_index_of(sub:str, text:str):
    result = re.findall(sub,text)
    if len(result) == 0:
        return -1
    else:
        return text.index(sub)


def my_copy(source, target):
    fileSource = open(source, "rb")
    content = fileSource.read()
    fileSource.close()
    fileTarget = open(target, "wb")
    fileTarget.write(content)
    fileTarget.close()


def my_move(source, target):
    os.rename(source, target)


def my_list(root):
    return os.listdir(root)


def my_match(text, query_re):
    result = re.findall(query_re, text)
    if(len(result)>0):
        return re.findall(query_re, text)[0]
    else:
        return ""


