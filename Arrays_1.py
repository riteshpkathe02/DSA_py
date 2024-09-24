exp = [2200,2350,2600,2130,2190]

print("In Feb, this much extra was spent compared to Jan", exp[1]-exp[0])

print("Total Expense in First quarter of the year",exp[0]+exp[1]+exp[2])

print("Did I spent $2000 in any month?", 2000 in exp)

exp.append(1980)
print("The expense of June is added to list: ", exp)

exp[3]=exp[3]-200
print("The refund got for order in April, updating expense",exp)