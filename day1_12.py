#by zxq
#对count清零，继续猜，输入n时退出
age_of_oldboy=56
count=0
while count<3:
    guess_age = int(input("guess age:"))
    if age_of_oldboy == guess_age:
        print("yes! you got it!")
        break
    elif age_of_oldboy < guess_age:
        print("think smaller...")
    else:
        print("think bigger..")
    count=count+1
    if count==3:
        countine_confirm=input("do you want to keep guessing..?")
        if countine_confirm != 'n':
            count=0
# else:
#     print("you have tried too many times... fuck off.")
