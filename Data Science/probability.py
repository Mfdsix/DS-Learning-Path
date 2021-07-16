from numpy import random
random.seed(0)

customers = 100000
ages = [ 20, 30, 40, 50, 60, 70 ]
totals = { 20:0, 30:0, 40:0, 50:0, 60:0, 70:0 }
purchases = { 20:0, 30:0, 40:0, 50:0, 60:0, 70:0 }
totalPurchases = 0

for _ in range(customers):
    age = random.choice(ages)
    probability = float(age) / 100
    totals[age] += 1

    if(random.random() < probability):
        purchases[age] += 1
        totalPurchases += 1

# look for probability of purchase of 30 years old customers
# E => 30s customer purchases
# F => 30 years old customers
selectedAge = 30
PE_bar_F = float(purchases[selectedAge]) / float(totals[selectedAge])
print('P(E|F): ', PE_bar_F)

# look for probability of 30 years old customers with all total customers
# F => 30 years old customers
PF = float(totals[selectedAge]) / customers
print('P(F): ', PF)

# look for probability of total purchases with all total customers
# E => all purchases
PE = float(totalPurchases) / customers
print('P(E): ', PE)

# but this is not relevant result. cause when we do P(E|F), it's just compared
# purchases from specific age (E), and customers with selected age (F)
# is't more fair when you compare (E) with all total customers
# so the notation is become P(E, F)
PEF = float(purchases[selectedAge]) / customers
print('P(E,F): ', PEF)

# combine results of PE and PF
PEPF = PE * PF
print('P(E)P(F): ', PEPF)

# prove that P(E,F) != P(E)P(F)
print('P(E,F) != P(E)P(F): ', PEF, ' != ', PEPF, (PEF == PEPF))

# prove that P(E|F) = P(E,F)/P(F)
print('P(E|F) = P(E,F)/P(F): ', PE_bar_F, ' = ', (PEF/PF), (PE_bar_F == PEF/PF))