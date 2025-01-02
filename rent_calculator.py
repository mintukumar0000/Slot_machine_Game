rent = int(input("Enter the rent you pay on manthly basis to your owner = "))
food = int(input("Enter the amount you guys are paid for the food = "))
electric = int(input("Enter the number of units spend= "))
bill_amount = int(input("Enter the charges of per unit = "))
total_bill = electric * bill_amount
person = int(input("Enter total number of rommet/flatmate you have = "))

output = (rent + food + total_bill)//person

print("Total bill for each person's- ", output)