from src import *
print("")

initial_salary_in_pence = int(input("What is your salary (in pence): "))

# gross pay
print("\nGross Pay:\t\t\t", format_currency(initial_salary_in_pence))

# calculate tax free allowance
result = tax_free_allowance(initial_salary_in_pence)
print("\nTax Free Allowance:\t\t", format_currency(result))

# calculate national insurance
result = total_national_insurance(initial_salary_in_pence)
print("\nNational Insurance Total:\t", format_currency(result))

# calculate taxable ammount
result = taxable_ammount(initial_salary_in_pence)
print("\nTaxable Ammount:\t\t", format_currency(result))

# total tax at 20%
result = tax_rate_at_20(taxable_ammount(initial_salary_in_pence))
print("\nTotal Tax at 20%:\t\t", format_currency(result))

# total tax at 40%
result = tax_rate_at_40(taxable_ammount(initial_salary_in_pence))
print("\nTotal Tax at 40%:\t\t", format_currency(result))

# # total tax at 45%
result = tax_rate_at_45(taxable_ammount(initial_salary_in_pence))
print("\nTotal Tax at 45%:\t\t", format_currency(result))

# total tax due
result = total_tax(initial_salary_in_pence)
print ("\nTotal Tax:\t\t\t", format_currency(result))

# calculate net wage
result = net_wage(initial_salary_in_pence)
print("\nNet Wage:\t\t\t", format_currency(result))

print(input("\nPress the anykey to exit."))
