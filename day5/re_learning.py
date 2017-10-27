#by zxq
#常用的正则表达式常用的模式，掌握模式后，可以用google。套路呀
#ex1：最简单的例子
import re
re.match("h^","hanmeimei")#匹配到值会有返回值，没匹配到none
res1=re.match("^h","hanmeimeihuhaifeng")
res2=re.search("hu[a-z]+g","hanmeimeihuhaifeng123")#中括号表示只匹配小写字母
print(res1)
print(res2)
