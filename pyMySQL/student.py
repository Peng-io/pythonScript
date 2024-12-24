import pymysql


class Studnet:
    def __init__(self) -> tuple:
        # 连接数据库
        self.comm = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            database="bishe",
            charset="utf8",
        )
        # 创建数据库的游标
        self.cursor = self.comm.cursor()


def insert():
    for i in range(50):
        sum += 1
        sql = "insert into student(id, password, name, age, sex, phone, room_no) value ('{sum}','123456','张三',)"


if __name__ == '__main__':
    studnet = Studnet()
    cursor = studnet.cursor
    comm = studnet.comm
    cursor.execute("SELECT * FROM student")
    # 读取全部数据
    num = 912200200
    for i in cursor.fetchall():
        num += 1
        no = '0' + str(num)
        cursor.execute(f"update student set id ='{no}'  where id = '{i[0]}'")
        comm.commit()
