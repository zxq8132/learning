#by zxq
#格式化拼接
name=input("name:")
age=int(input("age:"))
job=input("job:")
salary=input("salary:")
info='''
----------------info of {name} -----------
name:{name}
age:{age}
job:{job}
salary:{salary}
'''.format(name=name,age=age,job=job,salary=salary)
print(info)