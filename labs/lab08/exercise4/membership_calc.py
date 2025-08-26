'''
A fitness center offers monthly memberships. The base membership costs RM120 per month. Personal 
training sessions cost RM80 each, and a member wants to book 6 sessions. The gym also charges RM25 
for a locker rental and RM15 for towel service. There's a one-time registration fee of RM50 for new 
members. Calculate the total first-month cost, the monthly cost after the first month (without 
registration), and the annual cost (12 months including the first month). Use proper styling including 
variable names and comments.
'''

baseMembership = 120
personalTrainSes = 80
sessions = 6
lockerRent = 25
towelService = 15
oneTimeRegis = 50

# total first-month cost
totalFirstMonth = baseMembership + (personalTrainSes * sessions) + lockerRent + towelService + oneTimeRegis
print(f"Total first-month cost: RM{totalFirstMonth}")

# monthly cost after the first month (without registration)
totalOtherMonth = baseMembership + (personalTrainSes * sessions) + lockerRent + towelService
print(f"Monthly cost after the first month (without registration): RM{totalOtherMonth}")

# annual cost (12 months including the first month)
totalAnnual = totalFirstMonth + (totalOtherMonth * 11)
print(f"Annual cost (12 months including the first month): RM{totalAnnual}")