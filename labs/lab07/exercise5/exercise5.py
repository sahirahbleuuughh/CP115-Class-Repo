'''
Uses f-strings to display a comprehensive profile with:

    Basic personal information section
    String processing results
    Address information section
'''

import personal_data

print("CLIENT INFORMATION")
print(f"NAME: {personal_data.fullName}\nAGE: {personal_data.age}\nHEIGHT: {personal_data.weight}\nWEIGHT: {personal_data.height}")
print(f"PHONE NUMBER: {personal_data.phoneNum}\nEMAIL: {personal_data.email}\n")
print("STRING PROCESSED RESULTS")
print(f"UPPERCASE NAME: {personal_data.upperName}\nLOWERCASE NAME: {personal_data.lowerName}\nNAME LENGTH: {personal_data.nameLength}\n")
print("ADDRESS INFORMATION")
print(f"FULL ADDRESS: {personal_data.fullAddress}")