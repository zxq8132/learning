#by zxq
#全局变量中只有数字，字符串在函数内部不可以改，
# 列表、字典、集合、类是可以改的
cities=['shanghai','beijing','guanzhou']
def change_city():
    cities[1]="xi'an"
    print(cities)
change_city()
