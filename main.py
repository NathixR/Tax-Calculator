from src import *

gross_salary = None

while not gross_salary:
    try:
        gross_salary = float(input("\nWhat is your salary: "))
    except ValueError or NameError:
        print("You need to put in a number!")

# gross pay
result = gross_salary
print_row(
    "Gross Pay",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# calculate tax free allowance
result = tax_free_allowance(gross_salary)
print_row(
    "Tax Free Allowance",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# calculate national insurance
result = total_national_insurance(gross_salary)
print_row(
    "National Insurance",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# calculate taxable ammount
result = taxable_ammount(gross_salary)
print_row(
    "Taxable Ammount",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# total tax at 20%
result = tax_rate_at_20(taxable_ammount(gross_salary))
print_row(
    "Total Tax at 20%",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# total tax at 40%
result = tax_rate_at_40(taxable_ammount(gross_salary))
print_row(
    "Total Tax at 40%",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# # total tax at 45%
result = tax_rate_at_45(taxable_ammount(gross_salary))
print_row(
    "Total Tax at 45%",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# total tax due
result = total_tax(gross_salary)
print_row(
    "Total Tax",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# total deductions
result = total_deductions(gross_salary)
print_row(
    "Total Deductions",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

# calculate net wage
result = net_wage(gross_salary)
print_row(
    "Net Wage",
    format_currency(result),
    format_currency(monthly_ammount(result)),
    format_currency(weekly_ammount(result)),
    format_currency(daily_ammount(result)),
    total_percentage(result, gross_salary)
)

print(input("\nPress the anykey to exit."))
