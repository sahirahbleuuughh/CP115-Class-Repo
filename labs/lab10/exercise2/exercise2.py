    # Base premium by age: Under 25 = RM2400, 25-50 = RM1800, Over 50 = RM2000
    # Accident penalty: 0 accidents = No penalty, 1-2 accidents = +RM300, 3+ accidents = +RM600
    # Good driver discount: No accidents = 10% off final premium

age = int(input())
accident_count = int(input())

# Your code here
# Base premium by age
base_premium = 0
if age < 25:
    base_premium = 2400
elif age >= 25 and age <= 50:
    base_premium = 1800
elif age > 50:
    base_premium = 2000

# Accident penalty
accident_penalty = 0
if accident_count == 0:
    accident_penalty = 0
elif accident_count == 1 or accident_count == 2:
    accident_penalty = 300
elif accident_count >= 3:
    accident_penalty = 600

# Good driver discount & total
discount_amount = 0
final_premium =  base_premium + accident_penalty
if accident_penalty == 0:
    discount_amount = 10
    final_premium = base_premium - (base_premium * (discount_amount/100))

print(base_premium)
print(final_premium)
print(discount_amount)