#by zxq
#字符串的拼接1----效率低下，开辟多块内存
name=input("name:")
age=input("age:")
job=input("job:")
salary=input("salery:")
info='''
-----------info of  + -----
name:'''+ age +'''
age:'''+ job
job:'''+ salary +'''

print(info)