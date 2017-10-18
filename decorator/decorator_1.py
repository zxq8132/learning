#by zxq
'''
装饰器本身是函数，目的是为了在不影响原来函数功能的基础上，增加其他功能
例如：人有脚，鞋是为了保护脚，鞋的作用就类似于装饰器
原则：
1、不能修改被装饰的源代码
2、不能修改原函数的调用方式
实现装饰器的知识准备：
1、函数即“变量”
2、高阶函数
    a、把一个函数名当作实参传给另外一个函数
    b、返回值中包含函数名
3、嵌套
高阶函数+嵌套函数=>装饰器
'''
import time

def timer(func):
    def warpper(*arg,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time in is %s" %(stop_time-start_time))
    return warpper
@timer

def func_1():
    '''定义函数1，模拟为运行'''
    time.sleep(2)
    print("in the func_1")

func_1()