num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score
current_score = 0
for num_rounds in range(1, num_rounds + 1):
    round_score = int(input())
    if (round_score <= 100):
        current_score = current_score + round_score
    else:
        current_score = current_score + round_score + (0.2 * round_score)

final_score = current_score
rounds_processed = num_rounds
print(f"{final_score:.1f}")
print(rounds_processed)