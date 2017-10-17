#by zxq
#函数内部调用函数本身叫递归（recursion）
# python最多内部调用997次数
#1、必须有一个明确结束条件
#2、递归效率不高
#3、每次递归，问题规模要比上次递归有所减少
def calc(i):
    print(i)
    if int(i/2)>0:
        return calc(i/2)
    print("--->>",i)

calc(5)
