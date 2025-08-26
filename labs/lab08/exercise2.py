'''
A group of 6 friends went to a restaurant. They ordered 3 main dishes at RM25 each, 2 appetizers 
at RM12 each, and 4 drinks at RM8 each. The restaurant charges a 10% service tax on the total bill, 
then adds a RM5 delivery fee. Finally, they want to split the bill equally among all friends. Calculate 
the amount each person needs to pay. Make sure to use BODMAS concept and use floor division to get 
the amount in whole ringgit (ignore cents).
'''
mainDishesPrice = 75
appetizerPrice = 24
drinkPrice = 32

totalPrice = mainDishesPrice + appetizerPrice + drinkPrice

serviceTax = 0.1
deliveryFee = 5

finalPrice = ((0.1 * totalPrice) + totalPrice + deliveryFee)

# PER PERSON
floatDivFinal = finalPrice / 3
floorDivFinal = finalPrice // 3
intDivFinal = int(finalPrice / 3)

print(f"{finalPrice}")

print(f"{floatDivFinal}")
print(f"{floorDivFinal}")
print(f"{intDivFinal}\n")

###################################################################################################

mainDishesPrice = 75
appetizerPrice = 24
drinkPrice = 32

serviceTax = 0.1
deliveryFee = 5

finalPrice = ((serviceTax * (mainDishesPrice + appetizerPrice + drinkPrice)) + (mainDishesPrice + appetizerPrice + drinkPrice) + deliveryFee)

# PER PERSON
floatDivFinal = finalPrice / 3
floorDivFinal = finalPrice // 3
intDivFinal = int(finalPrice / 3)

print(f"{finalPrice}")

print(f"{floatDivFinal}")
print(f"{floorDivFinal}")
print(f"{intDivFinal}")