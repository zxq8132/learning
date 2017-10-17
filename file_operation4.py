#by zxq
f=open('my_heart_will_go_on','r',encoding='utf-8')#f 是文件句柄，默认是只读模式r，w是写模式——创建方式，会覆盖文件本身
#a是append追加模式不会覆盖原文件本身
# print(f.tell())#文件打开在什么位置。0代表在文件列表开头字符
# print(f.readline())
# print(f.readline())
# print(f.tell())#按字符的个数计数的
# print(f.seek(0))#回到文件字符的开始位置
# print(f.readline())
'''flush
import sys,time
for i in range(50):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)
'''
