# Business Requirement
### Create a program called TIP CALCULATOR
### It should ask for  total bill, number of people paying the bill, percentage contribution
### by each people and generate the amount to be pay by each.

print(" WELCOME TO THE TIP CALCULATOR")

total_bill = float(input("Enter the total bill? $"))
number_of_people = int(input("Enter how many people paying the bill?  "))
tip_percent = float(input(" Enter the percentage you want to pay? "))
cal_tip_percent = (tip_percent / 100) + 1
#print(cal_percent_payable)
tip_per_person = (total_bill * cal_tip_percent) / number_of_people
print(f'Each person should pay $ {round(tip_per_person, 2)} ')

