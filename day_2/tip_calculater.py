print("wellcome to tip calculater!")
Total_bill =float( input("what is the total bill?:"))
tip = int(input("how tip to provaid \n 10,20,30 \n how much:"))
people = int(input("how many people to split bill?:"))
bill_with_tip = tip / 100 * Total_bill + Total_bill
print("total bill",bill_with_tip)
each_person = round(bill_with_tip / people)
print(f"nandhu{each_person},saleem{each_person}")