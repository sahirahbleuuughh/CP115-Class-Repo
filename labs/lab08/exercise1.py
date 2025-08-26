'''
    Create these variables: score1 = 85, score2 = 92.5, score3 = 78
    Calculate the average of all three scores and print both the result and its type
    Convert the average to an integer using int() and print the difference from the original average
    Perform this calculation: score1 ** 2 / score2 + score3 % 7 and print the result and type
    Compare what happens with: int(score2) vs float(score1), why the results is liek that?
'''

score1 = 85
score2 = 92.5
score3 = 78

averageScore = (score1 + score2 + score3)/3
print(f"Original: {averageScore}, {type(averageScore)}")
averageScoreInt = int(averageScore)
print(f"Modified to Int: {averageScoreInt}, {type(averageScoreInt)}")

calc = score1 ** 2 / score2 + score3 % 7
print (f"{calc}, {type(calc)}")

intScore2 = int(score2) # rounded to the floor value (?)
floatScore1 = float(score1) # turning it into a fraction (have decimal number?)
# because we converted it to that type using the casing int() and float()

print(f"{intScore2} VS {floatScore1}")