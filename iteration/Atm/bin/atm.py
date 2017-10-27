#by zxq
#环境变量的写法，动态获取绝对路径
import os
import sys
# print(__file__)#打印文件的相对路径，看到绝对路径是因为在pycharm中
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)#添加环境变量
from conf import settings
from core import main
#main.login()