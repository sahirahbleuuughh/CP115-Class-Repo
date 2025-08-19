'''
    Import random and math modules
    Personal information variables:
        Full name, age, height (cm), weight (kg)
        Phone number, email address
        Street address, city, postcode
    String operations:
        Full name in UPPERCASE and lowercase
        Length of full name
        City name in UPPERCASE
        Full address (combine street + city + postcode)
        Length of full address
'''
import random
import math

#PERSONAL INFO
fullName = "Sahirah Alakazam"
age = 21
height = 200
weight = 2

phoneNum = "014-tekan-tekan-tak-dapat"
email = "nursahirahribin@gmail.com"

street = "Kg Rajunah"
city = "Kota Belud"
postcode = 89130

#FORMATTING
upperName = fullName.upper()
lowerName = fullName.lower()
nameLength = len(fullName)
upperCity = city.upper()
fullAddress = f"{street},{city}, {postcode}"
fullAddressLength = len(fullAddress)