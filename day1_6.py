#by zxq
#猜年龄，注意输入的数字默认是字符串
age_of_oldboy="56"
guess_age = input("guess age:")
if guess_age == age_of_oldboy:
    print("yes! you got it.")
elif guess_age > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger!")
