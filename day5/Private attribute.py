#by zxq
#用特定的方法才能改变的属性：Private attribute
class dog():#类名
    #定义一个类dog类
    n=123#类变量，可以节省开销
    name="我是类变量name"#实例变量中没有就会找类变量
    def __init__(self,name,state,skin,age):#构造函数，实例本省
        #在实例化时做类的初始化工作
        self.name=name#实例变量（静态属性）——相对的是类变量
        self.state=state
        self.skin=skin
        self.__age=age#将age设置为是私有属性
    #def __del__(self):#析构函数的作用构造函数的正好相反。它是在实例释放和销毁时
        #print("%s 跑到终点了"%self.name)
        #做一些收尾工作，如：关闭一些数据库链接打开的临时文件

    def state(self):#类的方法，（动态属性）
        print("它%s汪汪……"%self.state)
    def dog_name(self):
        print("%s 是个漂亮的小狗"%self.name)
    def dog_skin(self):
        print("是%s颜色的 "%self.skin)
    def dog_age(self):
        print("今年%s岁了"%self.age)
    def show_age(self):#定义一个方法，访问私有变量age.私有方法定义也是用__
        print("名字为:%s的小狗的年龄是%s"%(self.name,self.__age))
d1=dog("旺财","欢快的","摇尾巴","一岁")#d1是dog这个类的实例
print(d1.show_age())