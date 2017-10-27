#by zxq
#类的继承方式：breadth first广度优先，继承按照B——C——A的顺序
class A(object):
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    # def __init__(self):
    #     print("C")
class D(B,C):
    pass
obj=D()