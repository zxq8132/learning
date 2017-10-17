#by zxq
#循环执行 for
age_of_oldboy=56
for i in range(3):
    guess_age = int(input("guess age:"))
    if age_of_oldboy == guess_age:
        print("yes! you got it!")
        break
    elif age_of_oldboy < guess_age:
        print("think smaller...")
    else:
        print("think bigger..")
else:
    print("you have tried too many times... fuck off.")