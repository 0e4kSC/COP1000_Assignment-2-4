stateTax = salary * 0.065  # 6.5% state tax rate
federalTax = salary * 0.28  # 28% federal tax rate
dependents = min(numDependents * 1500.0, 4500.0)  # $1,500 per dependent, capped at $4,500

# Calculate take-home pay
takeHomePay = salary - stateTax - federalTax + dependents

# Display results
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependents))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
