num_days = int(input())
danger_threshold = float(input())

# TODO: Your code here
# Use input() inside the loop to get each day's temperature
counter = 1
danger_days = 0
temperature_sum = 0
while(counter <= num_days):
    temperature = float(input())
    days = counter
    if temperature > danger_threshold:
        danger_days += 1
    temperature_sum += temperature
    counter += 1

average_temp = temperature_sum / num_days
print(danger_days)
print(f"{average_temp:.1f}")