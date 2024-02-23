import re

text = "Google Runoob 123Taobao"
result = re.findall(r"\w+", text)
print(result)
