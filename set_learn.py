'''set集合可以用[ ]创建，也可以用{ }创建'''
'''set(集合)是一个非常有用的数据结构。它与列表(list)的行为类似，区别在于set不能包含重复的值。
这在很多情况下非常有用。例如你可能想检查列表中是否包含重复的元素'''
'''交集（intersection）对比两个集合的交集（两个集合中都有的数据）:'''
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
'''差集(difference)找出无效的数据，相当于用一个集合减去另一个集合的数据，'''
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))