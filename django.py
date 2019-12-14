'''dic={}

fill='y'
while fill=='y':
    keys=input("enter the key")
    val = input("enter the value")
    dic[keys]=val
    choice=input("enter y to continue or n to quit")
    if choice=='y' or choice=="Y":
        fill=fill
    else:
        fill='n'
print(dic)'''




import re
email=input("enter the email")
pattern='^.*@.*$'
find=re.match(pattern,email)
while True:
    if find:
        print("congratulation")
        break
    else:
        email = input("enter the email")
        find = re.match(pattern, email)





