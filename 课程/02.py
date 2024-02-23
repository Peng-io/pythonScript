list_data=[["张晓","男",26,"本科","985"],["刘蓓","女",31,"硕士","双非"],["李慧","女",24,"本科","211"],["彭松浩","男",20,"本科","双非"],
["陈理顺","男",20,"本科","双非"],["林天庄","男",20,"大专","双非"],["李惊鸿","男",20,"本科","双非"],["李凤强","男",80,"硕士","211"],
["郭传龙","男",30,"博士",985],["刘涛","女",21,"硕士",211],["张寒","男","21","中专","双非"]]
list_resume=[] #简历
list_candidate=[] #候选
list_interview=[] #面试
tuple_data=(("本科","硕士","博士"),(30,),("985","211"))
for data in list_data:
    if data[3]==tuple_data[0][0] or data[3]==tuple_data[0][1] or data[3]==tuple_data[0][2]:
        if data[2]<=tuple_data[1][0]:
            if data[4]==tuple_data[2][0] or data[4]==tuple_data[2][1]:
                list_interview.append(data)
            else :list_candidate.append(data)
        else :list_resume.append(data)
list_resume=tuple(list_resume)
list_candidate=tuple(list_candidate)
list_interview=tuple(list_interview)
print("简历库有{}人,分别是：{}".format(len(list_resume),list_resume),end="\n")
print("候选名单有{}人,分别是：{}".format(len(list_candidate),list_candidate),end="\n")
print("面试名单有{}人,分别是：{}".format(len(list_interview),list_interview),end="\n")
