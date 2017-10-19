#by zxq
#如何做并行
#生产者-消费者模型
import  time
def consumer(name):
    print("%s 消费者吃包子！" %name)
    while True:
        baozi=yield#保存当前状态
        print("包子[%s]来了，被[%s]" %(baozi,name))
# c_1=consumer("小明")
# c_1.__next__()
#
# b1="韭菜馅"
# c_1.send(b1)#给yield传值，__next()__只调用yield，不传值

def producer(name):
     c_1=consumer('A')
     c_2 = consumer('B')
     c_1.__next__()
     c_2.__next__()
     print("厨师开始做包子")
     for i in range(10):
         time.sleep(2)
         print("%s做了%s包子"%(name,i))
         c_1.send(i)
         c_2.send(i)

producer("zxq")
#通过iter()的方法，可以使迭代对象编程迭代器，使用__next__的方法
print(range(10))#range()本身就是一个迭代器