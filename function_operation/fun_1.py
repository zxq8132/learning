#by zxq
#用函数调用函数，不可以向上调用
def logger(source):
    '''打印日志，谁调用了它'''
    print("from %s"% source)

def test (name,age,*args,**kwargs):
    '''函数test内部调用logger函数，
    注意函数是有次序的，必须先定义logger
    test函数才能调用'''
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test")
    print("-------\n")

test('zxq','18','m','uuuu')
def tow_parameter (host,port=3306):
    '''默认形式参数有默认值时，调用时，
       实参可以不用传值。
    用途：1、默认好安装路径
          2、默认数据库连接参数'''
    print(host)
    print(port)

tow_parameter('127.0.0.1')

def many_parmeter(*args):
    '''形式参数固定数量的，实参数量和形参必须对应
       如果实参不确定，形参如何定义？
       用：参数组的定义，
       样式：*变量名'''
    print(args)#将值作为一个元组形式输出了

many_parmeter(1,2,3,4,5,6,7)

def many_parmeter2(x,*args):
    '''定义数组为形参，
        数组形参：接收n个位置参数，
        也就是说必须是数字
        转换为元组方式'''
    print('--------\n',x)
    print(args)

many_parmeter2(1,2,3,4,8)

def dic_parmeter(x,**kwargs):
    '''定义字典作为形参
    字典形参：接收n个关键字参数
    转换为字典方式'''
    print('--------\n', x)
    print(kwargs)

dic_parmeter(2017,name='zxq',age='36',gender='男')