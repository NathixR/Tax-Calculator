# define constants for calculations
TAX_RATE_20 = 20
TAX_RATE_40 = 40
TAX_RATE_45 = 45
NI_LOWER_THRESHOLD = 8060.00
NI_UPPER_THRESHOLD = 43000.00
NI_LOWER_RATE = 12
NI_UPPER_RATE = 2
TAX_FREE_ALLOWANCE = 11000.00
TAX_FREE_LOWER_THRESHOLD = 100000.00
TAX_FREE_UPPER_THRESHOLD = 122000.00
TAX_RATE_40_THRESHOLD = 32000.00
TAX_RATE_45_THRESHOLD = 150000.00

# formats the result in pounds
def format_currency(priceInPence):
    return "£{0:.2f}".format(priceInPence)

# formats the printed results
def print_row(title, value, monthly, weekly, daily, percentage):
    print("\n%s:\n%-12s%-12s%-12s%-12s%i%%" % \
    (title, value, monthly, weekly, daily, int(percentage)))

# calculates and displays the percentage of overall wages
def total_percentage(value, initial_salary):
    return (value / initial_salary) * 100

# calculates monthly ammount, so result devided by 12
def monthly_ammount(result):
    return result / 12

# calculate weekly ammount, so result divided by 52
def weekly_ammount(result):
    return result / 52

# calculates the daily ammount, so divides the result by 260
def daily_ammount(result):
    return result / 260

# calculate lower national insurance
def lower_national_insurance(full_salary):
    # if below lower threshold, nothing to pay
    if full_salary <= NI_LOWER_THRESHOLD:
        return 0
    # if below upper threshold, pay the lower rate on salary minus lower limit
    elif full_salary <= NI_UPPER_THRESHOLD:
        ratable_amount = full_salary - NI_LOWER_THRESHOLD
        return ratable_amount * (NI_LOWER_RATE / 100)
    # else pay the lower rate on salary between lower and upper limit
    else:
        ratable_amount = NI_UPPER_THRESHOLD - NI_LOWER_THRESHOLD
        return ratable_amount * (NI_LOWER_RATE / 100)

# calculate upper national insurance
def upper_national_insurance(full_salary):
    # if below higher threshold, nothing to pay
    if full_salary <= NI_UPPER_THRESHOLD:
        return 0
    # if above the threshold, pay rate on salary above the upper threshold
    else:
        ratable_amount = full_salary - NI_UPPER_THRESHOLD
        return ratable_amount * (NI_UPPER_RATE / 100)

# calculate total national insurance
def total_national_insurance(full_salary):
    lower = lower_national_insurance(full_salary)
    upper = upper_national_insurance(full_salary)
    total = lower + upper
    return total

# calculate tax free allowance
def tax_free_allowance(full_salary):
    if full_salary > TAX_FREE_UPPER_THRESHOLD:
        return 0
    # calculates the ammount to pay if between the £100,000 and £122,000 bracket
    # for every £1 above 100,000, £2 is deducted from allowance
    elif full_salary > TAX_FREE_LOWER_THRESHOLD:
        offset = (full_salary - TAX_FREE_LOWER_THRESHOLD) / 2
        return TAX_FREE_ALLOWANCE - offset
    elif full_salary >= TAX_FREE_ALLOWANCE:
        return TAX_FREE_ALLOWANCE
    else:
        return full_salary

# calculate taxable ammount
def taxable_ammount(full_salary):
    return full_salary - tax_free_allowance(full_salary)

# tax at 20% rate
def tax_rate_at_20(total_taxable):
    #
    if total_taxable <= TAX_FREE_ALLOWANCE:
        return 0
    elif total_taxable <= TAX_RATE_40_THRESHOLD:
        return total_taxable * (TAX_RATE_20 / 100)
    else:
        taxable = TAX_RATE_40_THRESHOLD
        return taxable * (TAX_RATE_20 / 100)

# tax at 40%
def tax_rate_at_40(total_taxable):
    if total_taxable <= TAX_RATE_40_THRESHOLD:
        return 0
    elif total_taxable <= TAX_RATE_45_THRESHOLD:
        taxable = total_taxable - TAX_RATE_40_THRESHOLD
        return taxable * (TAX_RATE_40 / 100)
    else:
        taxable = TAX_RATE_45_THRESHOLD - TAX_RATE_40_THRESHOLD
        return taxable * (TAX_RATE_40 / 100)

# tax at 45%
def tax_rate_at_45(total_taxable):
    if total_taxable <= TAX_RATE_45_THRESHOLD:
        return 0
    else:
        taxable = total_taxable - TAX_RATE_45_THRESHOLD
        return taxable * (TAX_RATE_45 / 100)

# calculate total tax
def total_tax(full_salary):
    total_taxable = taxable_ammount(full_salary)
    taxat20 = tax_rate_at_20(total_taxable)
    taxat40 = tax_rate_at_40(total_taxable)
    taxat45 = tax_rate_at_45(total_taxable)
    total = taxat20 + taxat40 + taxat45
    return total

# calculate total deductions
def total_deductions(full_salary):
    return full_salary - net_wage(full_salary)

# calculate net wage
def net_wage(full_salary):
    ni = total_national_insurance(full_salary)
    tax = total_tax(full_salary)
    total = full_salary - ni - tax
    return total
