#by zxq
#对于有规律的数据定义可以采用迭代（iteration），节省内存
# a=[]
# for i in range(10):
#     a.append(i*2)
# print(a)
#以上功能用生成器代替，代码如下：
b=(i*2 for i in range(10))#定义结构是用（）
print(b)#b就是生成器，不访问内存，不占用内存
for i in b:#调用生成器（generator）,不调用不生成
    print(i)
#生成器的方法,__next__()只保留一个值
