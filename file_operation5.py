#by zxq
#二进制，rb，先创建文件a.text
f=open('a','wb')#文件句柄，二进制编码文件-写
f.write('二进制文件写入的\n'.encode())#想写入，要转换成二进制格式
f.close()
f=open('a','rb')#文件句柄，二进制编码文件-读
print(f.readline().decode())#读取二进制文件,转化为utf-8




