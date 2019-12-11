dic={}

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
print(dic)


