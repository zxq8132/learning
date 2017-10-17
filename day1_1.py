#by zxq
name=input("name:")
age=int(input("age:"))
job=input("job:")
salary=input("salary:")
info='''
---------info of %s ----------
name:%s
age:%d
job:%s
salary:%s
''' % (name,name,age,job,salary)
print(info)