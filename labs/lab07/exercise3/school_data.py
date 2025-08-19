'''
    Student information variables (name, student ID, age)
    Course information variables (course code, course name)
    Import random module and generate two random scores (70-95 and 75-100)
    Calculate total score by adding the two scores
    String operations on student name (upper, lower, length)
    Import math module and calculate square root of total score
'''
import random
from math import sqrt

#STUDENT INFO
studentName = "John Doe"
studentID = "JD1832017"
studentAge = 42

#COURSE INFO
courseCode = "CP115"
courseName = "Coding Python"

#RANDOM INFO
scoreRandom1 = random.randint(70,95)
scoreRandom2 = random.randint(75,100)

#SCORE INFO
totalScore = scoreRandom1 + scoreRandom2

#STRING OPERATION INFO
upperName = studentName.upper()
lowerName = studentName.lower()
nameLength = len(studentName)

#MATH INFO
sqrtScore = sqrt(totalScore)