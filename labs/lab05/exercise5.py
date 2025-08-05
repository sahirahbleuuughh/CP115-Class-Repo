testScore1 = int(input("Enter English Test Result (out of 100): "))
testScore2 = int(input("Enter Math Test Result (out of 100): "))
testScore3 = int(input("Enter Physics Test Result (out of 100): "))

totalScore = float(testScore1 + testScore2 + testScore3)
averageScore = (totalScore/300)*100

print("English: ",testScore1)
print("Math: ",testScore2)
print("Physics: ",testScore3)
print("Total Score: ",totalScore)
print("Average Score: ",averageScore,"%")