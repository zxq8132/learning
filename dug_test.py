import pdb

def make_bread():
    '''启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
    pdb.set_trace()
    这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
    然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：'''
    pdb.set_trace()
    return "I don't have time"

print(make_bread())