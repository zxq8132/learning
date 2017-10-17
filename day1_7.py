#by zxq
#猜年龄，注意输入的数字默认是字符串
age_of_oldboy=56
guess_age=int(input("guess age:"))
if age_of_oldboy == guess_age:
    print("yes! you got it!")
elif age_of_oldboy < guess_age:
    print("think smaller...")
else:
    print("think bigger..")