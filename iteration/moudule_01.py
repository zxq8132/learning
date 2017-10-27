#by zxq
# 模块的分类：
# 一、标准库
# 1、时间模块
# time和datetime
# a、格式化表示的时间
# '2017-10-26-16:48:01'
# b、时间戳
# 本质就是秒数
# 从1970年01月01日0分0时0秒开始到当前的秒数
# ex1：
# import time
# x=time.time()#单位是秒
# print(x/3600/24/365)#1970+47=2017
# #c、 元组的表示方式
# print(time.localtime())
# print(time.timezone/3600)#和utc时间的差值
# print(help(time.gmtime()))
# y=time.localtime()
# print(time.mktime(y))#将元组表达方式的时间转换为时间戳
# print(time.strftime("%Y-%m-%d %H:%M:%S ",y))#格式化输出
# print(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime()))#定义格式就行，和位置无关
# print(time.asctime())#英文格式输出，如果没有传值，则默认本地时间信息
# print(time.ctime())#传入的是秒，和asctime接受的元组，ctime接受的是时间戳

import datetime#它是对time的高度封装
print(datetime.datetime.now())#获取当前时间
print(datetime.datetime.now()+datetime.timedelta(-3))#timedelta不能单独使用，要和now一起结合用
print(datetime.datetime.now()+datetime.timedelta(hours=-12))#timedelta不能单独使用，12小时前

# 二、开源模块
# 三、自定义模块