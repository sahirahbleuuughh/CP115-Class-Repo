'''
A student has taken 5 tests in a programming course. Their grades are 78, 85, 92, 67, and 88. The 
full mark is 100 for each test and a total of 500 for all test. Calculate the total points, average 
score, and what percentage each test contributes to the total score. Display the results showing each 
test score, total points, student average, and what percentage each test contributes to the total score. 
Use proper variable names and add comments explaining your calculations.
'''

test1 = 78
test2 = 85
test3 = 92
test4 = 67
test5 = 88

# calculate the sum of the score for all 5 tests
totalPoints = test1 + test2 + test3 + test4 + test5
# finds the average of the sum for all 5 tests
averageScore = totalPoints // 5

# checks what percentage does each test contributes to the totalPoints
test1Percent = int((78 / 500) * 100)
test2Percent = int((85 / 500) * 100)
test3Percent = int((92 / 500) * 100)
test4Percent = int((67 / 500) * 100)
test5Percent = int((88 / 500) * 100)

print(f"Test 1 Score: {test1}\nTest 2 Score: {test2}\nTest 3 Score: {test3}\nTest 4 Score: {test4}\nTest 5 Score: {test5}")
print(f"Total Points: {totalPoints}\n\nStudent Average: {averageScore}")
print(f"PERCENTAGE OF EACH TESTS\nTest 1: {test1Percent}%\nTest 2: {test2Percent}%\nTest 3: {test3Percent}%\nTest 4: {test4Percent}%\nTest 5: {test5Percent}%")