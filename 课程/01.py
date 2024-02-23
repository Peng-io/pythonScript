list_data=[["彭松浩","男",20,"广东省"],["陈理顺","男",20,"海南省"],["林天庄","男",20,"海南省"],["李惊鸿","男",20,"海南省"],
["李凤强","男",80,"贵州省"],["郭传龙","男",30,"福建省"],["刘涛","女",21,"江西省"]]
list_man=[]
list_gril=[]
list_address=[] #籍贯
list_30age=[] 
Max_sun=[] 
# print(len(list_data))
for i in list_data:
    list_address.append(i[3])
    Max_sun.append(i[2])
    if i[2]>=30 :
        list_30age.append(i)
    for j in i:
        if j=="男":
            list_man.append(i)
        elif  j=="女":
            list_gril.append(i)
        else :continue
Max_sun.sort()
print("男生有:{}人{}".format(len(list_man),list_man),end="\n")
print("女生有:{}人{}".format(len(list_gril),list_gril),end="\n")
print("年龄大于30岁的有:{}人分别是{}".format(len(list_30age),list_30age),end="\n")
print("年龄最大和最小的分别是:"+str(Max_sun[0])+"岁和"+str(Max_sun[-1])+"岁",end="\n")
print("所有的籍贯有{}".format(list_address))