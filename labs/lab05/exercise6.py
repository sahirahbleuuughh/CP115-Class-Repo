userTime = int(input("Enter time (in minutes): "))
convertedHour = round(float(userTime/60),2)
remainingMin = int(convertedHour%60)

print("Original Minutes: ",userTime, " minutes")
if remainingMin == 0:
    print("Converted Time: ",convertedHour," hours")
else:
    print("Converted Time: ",convertedHour," hours",remainingMin," minutes")

#will be changed im kinda lazy lol