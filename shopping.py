#by zxq
goods_list=[
    ('huaweiP9',3200),
    ('Macbook',6180),
    ('furongwang',225),
    ('chengguangCup',85),
    ('pythonbook',84)
]
shopping_list=[]
salary=input("请输入你的工资：")
if  salary.isdigit():
    salary=int(salary)
    print(goods_list)
    while True:
        # for index,item in enumerate(goods_list):
        for item in goods_list:
            print(goods_list.index(item),item)
        user_choice = input("选择要买的东西>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(goods_list) and user_choice >=0:
                p_item = goods_list[user_choice]
                if p_item[1] <= salary: #买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary) )
                else:
                    print("你的余额只剩%s啦，还买个毛线" % salary)
            else:
                print("你选择的商品序号 %s 不存在!"% user_choice)
        elif user_choice == 'q':
            print("--------购物清单------")
            for p in shopping_list:
                print(p)
            print("你的余额:",salary)
            exit()
        else:
            print("输入错误，退出输入q")