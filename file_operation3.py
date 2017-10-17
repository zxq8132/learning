#by zxq
#pycharm项目文件下，先创建文本文件my_heart_will_go_on
f=open('my_heart_will_go_on','r',encoding='utf-8')#f 是文件句柄，默认是只读模式r，w是写模式——创建方式，会覆盖文件本身
#a是append追加模式不会覆盖原文件本身
#不推荐写法
# for index,line in enumerate(f.readlines()):#readlines是所有行
#     if index==5:#列表枚举方式
#        print('---分割线------')#在第五行打印分割线,
#        continue
#     print(line.strip())
#推荐写法,效率高
count=0
for line in f:#按行打印，按迭代器的方式
    if count==5:
        print('---我是分割线----')
        count+= 1
        continue
    print(line)
    count += 1
