# define constants for calculations
TAX_RATE_20 = 20
TAX_RATE_40 = 40
TAX_RATE_45 = 45
NI_LOWER_THRESHOLD = 806000
NI_UPPER_THRESHOLD = 4300000
NI_LOWER_RATE = 12
NI_UPPER_RATE = 2
TAX_FREE_ALLOWANCE = 1100000
TAX_FREE_LOWER_THRESHOLD = 10000000
TAX_FREE_UPPER_THRESHOLD = 12200000
TAX_RATE_40_THRESHOLD = 3200000
TAX_RATE_45_THRESHOLD = 15000000

def format_currency(priceInPence):
    price = priceInPence / 100
    return "£{0:.2f}".format(price)

# calculate tax free allowance
def tax_free_allowance(full_salary):
    if full_salary > TAX_FREE_UPPER_THRESHOLD:
        return 0
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

# calculate lower national insurance
def lower_national_insurance(full_salary):
    if full_salary <= NI_LOWER_THRESHOLD: # if below threshold, nothing to pay
        return 0
    elif full_salary <= NI_UPPER_THRESHOLD: # if below upper limit, pay rate on salary minus lower limit
        ratable_amount = full_salary - NI_LOWER_THRESHOLD
        return ratable_amount * (NI_LOWER_RATE / 100)
    else: # if greater than upper limit, pay rate on salary below lower and upper limit
        ratable_amount = NI_UPPER_THRESHOLD - NI_LOWER_THRESHOLD
        return ratable_amount * (NI_LOWER_RATE / 100)

# calculate upper national insurance
def upper_national_insurance(full_salary):
    if full_salary <= NI_UPPER_THRESHOLD: # if below threshold, nothing to pay
        return 0
    else:
        ratable_amount = full_salary - NI_UPPER_THRESHOLD
        return ratable_amount * (NI_UPPER_RATE / 100)

# calculate total national insurance
def total_national_insurance(full_salary):
    lower = lower_national_insurance(full_salary)
    upper = upper_national_insurance(full_salary)
    total = lower + upper
    return total

# total tax
def total_tax(full_salary):
    total_taxable = taxable_ammount(full_salary)
    taxat20 = tax_rate_at_20(total_taxable)
    taxat40 = tax_rate_at_40(total_taxable)
    taxat45 = tax_rate_at_45(total_taxable)
    total = taxat20 + taxat40 + taxat45
    return total

# tax at 20%
def tax_rate_at_20(total_taxable):
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

# calculate net wage
def net_wage(full_salary):
    ni = total_national_insurance(full_salary)
    tax = total_tax(full_salary)
    total = full_salary - ni - tax
    return total
