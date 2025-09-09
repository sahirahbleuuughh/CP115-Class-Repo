employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
epf_deduct = 11
socso_deduct = 0.5
overtime_pay = 35

if (tax_status == "Single") and (base_salary >= 5000):
    tax_rate = 22
if (tax_status == "Single") and (base_salary < 5000):
    tax_rate = 18
if (tax_status == "Married") and (base_salary >= 6000):
    tax_rate = 20
if (tax_status == "Married") and (base_salary < 6000):
    tax_rate = 15
if (tax_status == "Head") and (base_salary >= 5500):
    tax_rate  = 25
if (tax_status == "Head") and (base_salary < 5500):
    tax_rate = 19

net_salary = (base_salary + (overtime_hours * overtime_pay)) * (100-tax_rate)/100 * (100-epf_deduct-socso_deduct)/100
print(employee_name)
print(f"{tax_rate}%")
print(f"{net_salary:.2f}")