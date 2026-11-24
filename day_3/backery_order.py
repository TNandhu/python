print("well come to sds backery")
chai=input("what you want like tea or coffee")
puff=input("and extra any think else like puff y or n:")

bill=0
if chai == "tea":
    bill +=20
elif chai == "coffee":
    bill +=25
else:
    print("sorry it will not availabe")

if puff =="y":
    puff_type = input("what type of puff you want (egg,veg,mus)")
    if puff_type =="egg":
        bill +=50
    elif puff_type =="veg":
        bill +=45
    elif puff_type =="mus":
        bill +=30
else:
    print("thank you")

print(bill)