#by zxq
#pycharm项目文件下，先创建文本文件my_heart_will_go_on
f=open('my_heart_will_go_on','a',encoding='utf-8')#f 是文件句柄，默认是只读模式r，w是写模式——创建方式，会覆盖文件本身
#a是append追加模式不会覆盖原文件本身，
# data=f.read()
# data2=f.read()
# print(data)
# print('----data2---%s--'%data2)#data2没有输出，是因为data将文件读到最后一行了，data2没有内容可读了
f.write('这一行是python追加过来的！')
