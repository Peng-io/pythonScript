import re

if __name__ == '__main__':
    text = "Google Runoob 123Taobao"
    result = re.findall(r"\w+", text)
    print(result)
