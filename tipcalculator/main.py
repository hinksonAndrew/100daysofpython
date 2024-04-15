# print welcome message
print("Welcome to the tip calculator!")

# ask the user how much the total bill is
total_bill = float(input("What was the total bill? $"))

# ask how much of a tip they would like to leave
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))

# ask how many people are splitting the bill
people_amount = int(input("How many people to split the bill? "))

# calculating total bill with tip included
bill_with_tip = total_bill * (1 + tip_amount / 100)

# dividing the bill_with_tip by how many ways it needs to split
per_person = bill_with_tip / people_amount

# rounding to 2 decimal places and making sure it always shows 2 decimals
final_amount = "{:.2f}".format(per_person)

# final message letting user know how much each person owes
print(f"Each person should pay: ${final_amount}")

