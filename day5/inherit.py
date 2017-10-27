#by zxq
#继承：在一个大的类下面包含小的类，通用的属性和方法不用再写，
# 继承的主要作用是为了节省代码
#class People:#经典类的写法
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
class Man(People):
    def __init__(self,name,age,beard):
        #People.__init__(self,name,age)#继承了父类People,当多继承时比较麻烦
        super(Man,self).__init__(name,age)#当父类改变名字时，不用改了，推荐写法
        self.beard=beard
    def grow_beard(self):
        print("%s%s岁的胡子%s厘米长"%(self.name,self.age,self.beard))
    def sleep(self):
        People.sleep(self)#重构的方法
        print("男人在休息")
m1=Man("李白","35","6")
m1.eat()
m1.talk()
m1.grow_beard()
class Woman(People):
    def get_birth(self):
        print("%s在生孩子"%self.name)
w1=Woman("卫子夫",19)
w1.get_birth()