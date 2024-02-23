import os

# 获取当前文件夹路径
path = os.getcwd()

# 列出当前文件夹下的所有文件和文件夹
files = os.listdir(path)

# 遍历每一个文件和文件夹
for file in files:
    # 判断是否是文件
    if os.path.isfile(file):
        # 如果是文件，则获取文件后缀并打印出来
        file_name, file_ext = os.path.splitext(file)
        print(file_ext)
