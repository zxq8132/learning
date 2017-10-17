#by zxq
#循环执行 while
age_of_oldboy=56
count=0
while True:
    if count == 3:
        print("you have tried too many times... fuck off.")
        break
    guess_age = int(input("guess age:"))
    if age_of_oldboy == guess_age:
        print("yes! you got it!")
        break
    elif age_of_oldboy < guess_age:
        print("think smaller...")
    else:
        print("think bigger..")
    count = count + 1
    print("You've got a 3 chance，Already in use", count)
