def Fanc(school,teacher,*args,major,Num=3,**kwargs):
    str=[]
    print("欢迎报考{}的{}专业".format(school,major),end="\n")
    print("{}专业的录取分数线为:{}目标招收:{}人".format(major,kwargs["分数线"],Num),end="\n")
    print("报考的考生有：")
    for i in args:
        print("姓名:{},成绩:{}".format(i[0],i[1]))
        if i[1]>=kwargs["分数线"]:
            str.append(i)
    print("招生的老师为：{}".format(teacher),end="\n")
    print("共计报考人数:{}。达线人数:{}".format(len(args),len(str)),end="\n")
    str.sort(key=lambda args : args[1],reverse=True)
    print("录取名单如下:{}".format(str[:Num]),end="\n")
Fanc("琼台师范学院",["刘涛","程俊"],["彭松浩",611],["张寒",599],["林天庄",601],["王力宏",602],["郭传龙",655],major="计算机科学与技术",分数线=600)
