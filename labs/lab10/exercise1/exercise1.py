    # Base hourly rates: Manager RM35, Supervisor RM25, Staff RM18
    # Overtime rate: 1.5x base rate for all overtime hours
    # Weekend bonus: Extra RM5 for each overtime hour worked on weekends, calculated separately from overtime pay and then added to total

position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
# Base hourly rates
hourly_rate = 0
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

# Overtime rate
overtime_pay = 0
if overtime_hours > 0:
    overtime_pay = (overtime_hours * (hourly_rate * 1.5))

# Weekend bonus
weekend_bonus = 5 * overtime_hours
total_pay = 0
if is_weekend == "Yes":
    total_pay = overtime_pay + weekend_bonus
elif is_weekend == "No":
    total_pay = overtime_pay

overtime_pay = total_pay
print(hourly_rate)
print(overtime_pay)
print(total_pay)