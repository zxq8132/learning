#by zxq
#pycharm项目文件下，先创建文本文件my_heart_will_go_on
f=open('my_heart_will_go_on','r',encoding='utf-8')#f 是文件句柄，默认是只读模式r，w是写模式——创建方式，会覆盖文件本身
#a是append追加模式不会覆盖原文件本身
print(f.readline())# 读一行
for line in f.readlines():#readlines是所有行
    print(line.strip())#循环打印全部文件