#by zxq
#斐波拉契数列的实现，用函数实现
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'end'
# fib(10)
#斐波拉契数列的生成器,关键字是yield
#函数值能连续输出，就可以用生成器的方式定义？
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'end'

a=fib(10)
print(a.__next__())
print("--------")
print(a.__next__())
print("--------")
print(a.__next__())
print("--------")
