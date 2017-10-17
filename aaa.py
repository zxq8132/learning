#by zxq
with open('a','w',encoding='utf-8') as f,\
    open('some_file','r',encoding='utf-8') as f_new:
    f.write('Hello ')
    f.write('World')