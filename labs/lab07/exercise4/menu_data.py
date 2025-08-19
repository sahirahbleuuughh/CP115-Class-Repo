'''
    Import the random module
    Create variables for:
        Restaurant name (your choice)
        Restaurant location
        Three menu items with names only (no prices or calculations)
    Use string operations to create:
        Restaurant name in uppercase
        Restaurant name in lowercase
        Length of the location name
    Use random to generate:
        A daily special number (1, 2, or 3)
        A customer number (between 100-999)
'''
import random

#RESTAURANT INFO
restaurantName = "In-N-Out" 
restaurantLocation = "Bermuda Triangle"
food = "Big Ass Steak"
drink = "Tiny Soda"
dessert = "Barbeque Chicken"

#FORMATING
upperRestaurant = restaurantName.upper()
lowerRestaurant = restaurantName.lower()
restaurantLength = len(restaurantName)

#RANDOMING
specialNumDaily = random.randint(1,3)
customerNum = random.randint(100,999)