def tax(weekly_pay):
    tax_free = 12500
    yearly_pay = weekly_pay * 52
    taxable_pay = yearly_pay - tax_free
    yearly_tax_paid = taxable_pay * 0.2
    tax_paid = yearly_tax_paid / 52
    return tax_paid

def ni(weekly_pay):
    deduct_pay = weekly_pay - 183
    ni_cont = deduct_pay * 0.12
    return ni_cont

mon_hours = float(input("How many hours did you work Monday: "))
tue_hours = float(input("How many hours did you work Tuesday: "))
wed_hours = float(input("How many hours did you work Wednesday: "))
thur_hours = float(input("How many hours did you work Thursday: "))
fri_hours = float(input("How many hours did you work Friday: "))
sat_hours = float(input("How many hours did you work Saturday: "))
sun_hours = float(input("How many hours did you work Sunday: "))

total_hours = mon_hours + tue_hours + wed_hours + thur_hours + fri_hours + sat_hours + sun_hours

hourly_wage = float(input("What is your hourly wage: "))

days_worked = 0

if mon_hours > 0:
    days_worked += 1

if tue_hours > 0:
    days_worked += 1

if wed_hours > 0:
    days_worked += 1

if thur_hours > 0:
    days_worked += 1

if fri_hours > 0:
    days_worked += 1

if sat_hours > 0:
    days_worked += 1

if sun_hours > 0:
    days_worked += 1

breaks = days_worked * 0.5

total_hour_after_breaks = total_hours - breaks

pretax_pay = total_hour_after_breaks * hourly_wage

pay_after_tax = pretax_pay - tax(pretax_pay)

pay_after_ni = pay_after_tax - ni(pretax_pay)#

other_deductions = 31.94

total_after_deduct = pay_after_ni - other_deductions

print("This week you earned: £" + str(total_after_deduct))
print(tax(pretax_pay))
print(ni(pretax_pay))


