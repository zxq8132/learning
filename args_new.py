'''*args 的用法

*args 和 **kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。
*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
例子:'''
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')