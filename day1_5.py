#by zxq
import getpass
_username='zxq'
_password='zxq8132'
username=input("username:")
#password=getpass.getpass("password:")
password=input("password:")
if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")
print(username,password)