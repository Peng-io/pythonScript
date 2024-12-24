import re

if __name__ == '__main__':
    file_regex = re.compile(r'\.(\w+)$')

    file_name = '01.jpg'
    match_obj = file_regex.search(file_name)

    if match_obj:
        file_type = match_obj.group(1)
        print(file_type)
    else:
        print('未匹配到文件类型')
