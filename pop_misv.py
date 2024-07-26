import random
import numpy as np

#5 is arbitrary
investor_guesses_sd = 5

#8-22 establishes a dictionary of all the securities, their fake_values, and their prices
#initializing
securities = {}
security_names = []

n_securities = 2 #I can choose this

#make a list of n securities
for i in range(n_securities):
    security_names.append(f"security{i}")

#use the list of n investor names as keys in the investors dictionary, with values that 
#are randomly generated estimates of security 1's fake value
for name in security_names:
    securities[name] = {"fake_value": random.randrange(0,100), #cap at 100 is arbitrary (should this be a normal distribution?)
                        "price": random.randrange(0,100)} #cap at 100 is arbitrary (should this be a normal distribution?)



#27-30 makes a dictionary with the perfect investor's valuation on all the securities (at some point it may make sense to add this to the investors dictionary)
perfect_fv_investor = {}

for security in security_names:
     perfect_fv_investor[f"{security}_estimate"]  = securities[security]["fake_value"] 


#34-49 establishes a dictionary of investors, each of whom has estimates of the fake_value of each security
#initializing
investors = {}
investor_names = []

n_investors = 2 #I can choose this

#make a list of n investor names
for i in range(n_investors):
    investor_names.append(f"investor{i}")

#use the list of n investor names as keys in the investors dictionary, with values that 
#are randomly generated estimates of security n's fake value
for name in investor_names:
    investors[name] = {}
    for security in security_names:
        investors[name][f"{security}_estimate"] = np.random.normal(securities[security]["fake_value"],investor_guesses_sd)



""" If you want to test"""

print(f"Securities: {securities}")
print(f"Perfect Investor: {perfect_fv_investor}")
print(f"Investors: {investors}")
print()

def should_buy(investor,security):
    if securities[security]["price"] < investors[investor][f"{security}_estimate"]:
        return "buy"
    else:
        return "not buy"

for investor in investors:
    for security in securities:
        print(f'{investor} should {should_buy(investor,security)} {security}')
        print(f'Price: {securities[security]["price"]}     Estimate: {investors[investor][f"{security}_estimate"]}')
        print()