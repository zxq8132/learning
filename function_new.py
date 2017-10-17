def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
print(a())
'''如果要返回welcome呢？'''
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome
'''注意name="ali"后的函数返回值'''
a = hi(name = "ali")
print(a)
print(a())
'''注意：hi()()的作用'''
print(hi()())