### os

### 默认状态下，os.getcwd()输出的是当前正在编辑py文件所在的路径。

```python
import os

print(os.getcwd())
```

### 获取路径中的最后一个文件夹名字。

```python
import os

os.path.basename("path") 
```

### 获取桌面的路径

```text
import os
os.path.expanduser("~")   
获取电脑用户名及路径

```

获取到用户名的路径后，用os.path.join()拼接即可获得桌面路径。

```python
import os

user = os.path.expanduser("~")
desktop = os.path.join(user, 'Desktop')
print(user)
print(desktop)
```

### 判断路径 path是否存在。

```python
import os

os.path.exists("path")
```

### 前者判断path是否为文件夹，后者判断path是否为文件。

```python
import os

os.path.isdir("path")
os.path.isfile("path")
```

### 输出path路径下所有文件及文件夹，返回结果为一个列表。（不遍历下层）

```python
import os

os.listdir(path="path")
# 当不传入 path时，有两种情况：①若没有设置 os.chdir(path)去指定默认路径，则输出当前代码文件所在目录下的文件及文件夹。
# ②若设置了 os.chdir(path1)，则输出该path1路径下的文件及文件夹。
# “ 不遍历嵌套文件夹 ” 意思是：即使merge文件夹下还有文件，那么这个文件也不会得到输出，即仅遍历当前层。
```

### 循环遍历top路径下的所有文件，该路径下层的文件及文件夹。

```python
import os

os.walk("top", topdown=True, οnerrοr=None, followlinks=False)
# top：路径，顶层路径
# topdown：可以理解为加快速度，不用管，默认为True
# onerror：当有错误时，可以用定义的函数去输出错误
# followlinks：默认为False，意义不大

# 该函数必须传入路径，返回3个变量值。
# 第一个为文件夹绝对路径，
# 第二个为子文件夹的列表，
# 第三个为根目录下所有文件的列表。
```

### scandir

```python
import os

for i in os.scandir(r'path'):
    print(i)
    print(i.name)
    print(i.path)
    print(i.is_dir())
    print(i.is_file())
    print('-' * 70)
# 还可以访问文件的各种属性。
# 如获取文件/文件夹名，文件/文件夹绝对路径，是否为文件夹，是否为文件，以及属性。
```

|文件大小 | st_size|
|--- | ---|
|最近访问时间|st_atime|
|最近修改时间|st_mtime|

```text
加快迭代速度，把需要迭代的内容放在一个迭代对象里，
而不是像os.listdir()一样把结果存在列表中（放在列表占用大量内存）
```

### 获得文件的属性。

```python
import os

os.stat("path")
```

### 创建路径（文件夹），若该路径已存在，则报错。（只能创建一层）

```python
import os

os.mkdir("path", mode=511)
```

### 重命名/移动文件或文件夹。

```python
import os

os.rename("src", "dst")
# src：原文件路径
# dst：重命名 / 移动后的文件路径
```

### 删除文件。

```python
import os

os.remove("path")
# 小心该操作，不进回收站，删除后是很难找回来的，建议不要用重要的文件去实验。
```