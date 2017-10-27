#by zxq
#多继承
class People(object):#新式类的写法，推荐使用
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("%s在享受美食"%self.name)
    def talk(self):
        print("%s在作诗"%self.name)
    def sleep(self):
        print("%s在睡觉"%self.name)

class Communication(object):
    #定义一个Blind父类
    def meet(self,obj):
        print("%s找%s交流诗词" %(self.name,obj.name))

class Man(People,Communication):#多继承，People,Communication
    #定义了一个子类男人
    def __init__(self,name,age,beard):
        #People.__init__(self,name,age)#继承了父类People,当多继承时比较麻烦
        super(Man,self).__init__(name,age)#当父类改变名字时，不用改了，推荐写法
        self.beard=beard
    def grow_beard(self):
        print("%s%s岁的胡子%s厘米长"%(self.name,self.age,self.beard))
    def sleep(self):
        #People.sleep(self)#通过父类，重构的方法，经典写法
        super(Man,self).sleep(self)#新式类的写法
        print("男人在休息")

class Woman(People,Communication):#多继承，People,Communication
    #定义一个子类女人
    def get_birth(self):
        print("%s在生孩子"%self.name)
w1=Woman("蔡文姬",32)
m1=Man("李白",32,5)
m1.meet(w1)#多继承的结果
w1.meet(m1)#多继承的结果

