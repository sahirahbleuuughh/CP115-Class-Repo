itemName = input("Enter item name: ")
itemPrice = round(float(input("Enter item price: ")),2)

itemQuantity = 3
taxRate = 6

subTotal = round(itemPrice * itemQuantity,2)
taxAmount = round((6/100)*subTotal,)
totalCost = round(subTotal + taxAmount,2)

print("Item: ",itemName)
print("Subtotal: RM",subTotal)
print("Tax Amount: RM",taxAmount)
print("Total Cost: RM",totalCost)