import os

import pymysql
from openpyxl import load_workbook

workbook = load_workbook(os.getcwd() + "./test.xlsx")
sheet = workbook.active


def get_data() -> tuple:
    # 连接数据库
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="bishe",
        charset="utf8",
    )
    # 创建数据库的游标
    cursor = db.cursor()
    # execute()方法并执行 SQL 语句
    cursor.execute("SELECT * FROM student")
    # 读取全部数据
    data = cursor.fetchall()
    # 关闭连接
    db.close()
    return data


def change_data() -> None:
    sheet['A2'] = '0001'
    workbook.save("test.xlsx")


def add_data():
    data = ["0005", "123456", "地瓜", "120", "3536", "1111"]
    sheet.append(data)
    workbook.save("test.xlsx")


if __name__ == "__main__":
    add_data()
