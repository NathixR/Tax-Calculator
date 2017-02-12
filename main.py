from src import *
print("")

initial_salary_in_pence = int(input("What is your salary (in pence): "))

# gross pay
print("Gross Pay:")
print(format_currency(initial_salary_in_pence))
print("")

# calculate tax free allowance
print("Tax Free Allowance:")
result = tax_free_allowance(initial_salary_in_pence)
print(format_currency(result))
print("")

# calculate taxable ammount
print("Taxable Ammount:")
result = taxable_ammount(initial_salary_in_pence)
print(format_currency(result))
print("")

# calculate national insurance
print("National Insurance Total:")
result = total_national_insurance(initial_salary_in_pence)
print(format_currency(result))
print("")

# tax at 20%
# tax at 40%
# tax at 45%
# total tax

# calculate net wage
print("Net Wage:")
result = net_wage(initial_salary_in_pence)
print(format_currency(result))
print("")
