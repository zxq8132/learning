#by zxq
#局部变量，只在函数里生效
gender='man'
def change_name(name):
    gender='woman'
    print("before change",name,gender)
    name='zrp'
    print("after chang",name)
name="zxq"
change_name(name)
print(name)
print(gender)
