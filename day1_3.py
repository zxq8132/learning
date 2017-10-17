#by zxq
#by zxq
#格式化拼接
name=input("name:")
age=int(input("age:"))
job=input("job:")
salary=input("salary:")
info='''
----------------info of {0} -----------
name:{0}
age:{1}
job:{2}
salary:{3}
'''.format(name,age,job,salary)
print(info)