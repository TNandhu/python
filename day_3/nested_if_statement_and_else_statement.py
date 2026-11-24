print("wellcome to the group shirt")
name = input("enter the name :")
print(name)
amount = int(input("enter the amount :"))
if amount >=800:
    print("they paid the amount fully")
    size = input("enter the size :")
    if size == "s":
        bill = 700
        print("shirt amount is 700")
    elif size =="m":
        bill = 750
        print("shirt amount is 750")
    elif size == "l":
        bill = 800
        print("shirt amount is 800")
    else:
        print("shirt amount is 800")
    bach = input("do you want the bach? type y or n")
    if bach =="y":
        bill +=25
    print(f"total bill{bill}")

else:
    print("they will be pending the amount")

            