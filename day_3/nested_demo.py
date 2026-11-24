print("wellcome to the roller coaster")
height = int(input("enter the height in cm :"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("enter your age :"))
    if age < 12:
        print("child ticket price is $5")
    elif age <= 18:
        print("youth ticket price is $7")
    else:
        print("adult ticket price is $12")
else:
    print("sorry you have to grow taller before you can ride")




a=int(input("enter the number :"))
if a < 20:
    print("greater than 20")
elif a ==20:
    print("equal to 20")
else:
    print("less than 20")
    