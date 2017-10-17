#by zxq
list_1=[1,2,3,4,5,5,1,2]
list_2=[3,4,5,3,6,4,7,8,9]
list_3=[1,2,3]
list_3=set(list_3)#变成集合
list_1=set(list_1)#变成集合
list_2=set(list_2)#变成集合
print(list_1,type(list_1))#去重打印
print(list_2,type(list_2))#去重打印
list_1.intersection(list_2)#取交集
print(list_1.intersection(list_2))#打印交集
a=list_1.union(list_2)#取并集
print(a)
b=list_1.difference(list_2)#取差集
c=list_2.difference(list_1)
print(b)
print(c)
print(list_3.issubset(list_1))#判断list_3是不是list_1的子集
print(list_1.issuperset(list_3))#判断list_1是不是list_3的父级
print(list_1.symmetric_difference(list_2))#把交集去掉，把其他的留下来，对称差集
print(list_1 & list_2)#交集
print(list_1 | list_2)#并集
print(list_1-list_2)#差集
print(list_1^list_2)#对称差集
print(list_3<list_1)#子集
print(list_1>list_3)#父级
print(list_1 and list_2)#什么意思呢？
#集合操作
list_1.add(123)#添加一项
print(list_1)
print(len(list_1))#打印元素数量
list_1.update([345,678,101])
print(list_1)#添加多项
print(len(list_1))#打印元素数量
print(1 in list_1)#判断元素是否在集合中
print(1 not in list_1)#判断元素是否在集合中
print(list_3.issubset(list_1))#判断list_3中的元素是否都在list_3中
print(list_1.pop())#随机删除。不能指定值
print(list_2.discard(3))#指定删除元素，discard不存在的元素不会报错
print(list_2.remove(4))#指定删除元素，remove的元素不存在会报错
print(list_2)
