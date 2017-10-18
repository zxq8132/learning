#by zxq
import  time
def bar():
    print("in the bar")

def func_1(func):
   start_time=time.time()
   func()
   stop_time=time.time()
   print("the func run time %s" %(stop_time-start_time))

func_1(bar)
