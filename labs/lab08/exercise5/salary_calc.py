'''
Access the data using employee_data.basic_salary, employee_data.overtime_hours, and 
employee_data.overtime_rate. 
Calculate the total salary with these deductions: 11% for EPF, 
0.5% for SOCSO, and 0.2% for EIS. Add fixed deductions of RM50 for medical insurance and RM30 
for parking. 
Display a payslip showing gross salary (basic + overtime), each deduction amount, 
total deductions, and net salary. Use proper formatting and comments.
'''
import employee_data

EPF = 0.11
SOCSO = 0.005
EIS = 0.002

medicalInsurance = 50
parking = 30

grossSalary = employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate)

EPFDeduct = EPF * grossSalary
SOCSODeduct = SOCSO * grossSalary
EISDeduct = EIS * grossSalary

totalDeduction = EPFDeduct + SOCSODeduct + EISDeduct + medicalInsurance + parking

netSalary = grossSalary - totalDeduction

print(f"Gross Salary: {grossSalary}\n")
print(f"EPF: {EPFDeduct}\nSOCSO: {SOCSODeduct}\nEIS: {EISDeduct}\n")
print(f"Total Deduction: {totalDeduction}\nNet Salary: {netSalary}")