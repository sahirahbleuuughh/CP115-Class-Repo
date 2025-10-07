score_input = input()

# TODO: Your code here
passing_count = 0
failing_count = 0
score_count = 0
while score_input != "end":
    if int(score_input) >= 60:
        passing_count += 1
    if int(score_input) < 60:
        failing_count += 1
    score_count += 1
    score_input = input()

if score_count != 0:
    pass_rate = (passing_count / score_count) * 100
else:
    pass_rate = 0

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
