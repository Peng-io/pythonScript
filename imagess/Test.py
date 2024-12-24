import os
import re

from PIL import Image

# 扫描当前文件夹下的所有jpg和png的图片并把像素全部改成640*427

# 获取当前文件夹路径
path = os.getcwd()
# 列出当前文件夹下的所有文件和文件夹
files = os.listdir(path)
file_list = []


def is_flag(file_name: str) -> bool:
    file_regex = re.compile(r"\.(\w+)$")
    match_obj = file_regex.search(file_name)
    if match_obj:
        file_type = match_obj.group(1)
        if file_type in ["png", "jpg"]:
            return True
        else:
            return False
    else:
        print("未匹配到文件类型")
        return False


# 遍历每一个文件和文件夹
for file in files:
    # 判断是否是图片
    if os.path.isfile(file) and is_flag(file):
        # 如果是文件，则进行相应的操作
        file_list.append(path + "\\" + file)

for i in file_list:
    img = Image.open(i)
    try:
        re_img = img.resize((640, 427))
        re_img.save(i)
        print(i + "图像调整成功!")
    except IOError:
        print(i + "图像调整失败!")
