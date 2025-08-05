import math

circleRadius = float(input("Enter radius: "))
circleArea = round(float(math.pi*(circleRadius**2)),4)
circleCircum = round(float(2*math.pi*circleRadius),4)

print("Area of circle: ", circleArea)
print("Circumference of circle: ", circleCircum)