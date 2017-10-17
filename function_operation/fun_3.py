#by zxq，
# 在函数内改全局变量，造成代码可读性非常差
gender='man'
def change_name(name):
    global gender#在函数内部，声明为同名全局变量，不推荐这么做
    gender = 'woman'
    print("before change",name,gender)
    name='zrp'
    print("after chang",name)
name="zxq"
change_name(name)
print(name)
print(gender)