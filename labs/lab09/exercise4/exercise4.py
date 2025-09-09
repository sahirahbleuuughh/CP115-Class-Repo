# Calculate water bills with tiered pricing based on consumption.

# Rate Structure:

#     First 20 cubic meters: RM0.57 per cubic meter
#     Next 15 cubic meters (21-35): RM1.03 per cubic meter
#     Above 35 cubic meters: RM1.40 per cubic meter

# Additional charges: Service charge RM8, Sewerage RM2

current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here
consumption = current_reading - previous_reading
service_charge = 8
sewerage = 2

if (consumption <= 20):
    water_cost = consumption * 0.57
elif (consumption > 20) and (consumption <= 35):
    water_cost = 11.4 + ((consumption - 20) * 1.03)
else:
    water_cost = 26.85 + ((consumption - 35) * 1.40)

total_bill = water_cost + service_charge + sewerage

print(consumption)
print(water_cost)
print(total_bill)