#by zxq
#循环执行 while
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
else:
    print("you have tried too many times... fuck off.")


