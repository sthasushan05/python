import sys
'''name=input("enter your name")
for x in range(1,100):
    if name.isalpha()==True and '' in name:
        if len(name)>=3:
            pass
        else:
            print("enter the correct name")
            name=input("name: ")
    else:
        print("enter the alphabet")
        name=input("name: ")
age=int(input("enter age"))
while age<15:
    print("enter the correct age")
    age=int(input("age"))
'''
mob_num=input("enter the phn number")
while len(mob_num)!=10 :
    if mob_num.isdecimal()==True:
        print("enter mob number")
        mob_num = input("mob_num: ")
    else:
         print("enter mob number")
         mob_num=input("mob_num: ")
