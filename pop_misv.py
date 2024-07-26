import random
import numpy as np

#5 is arbitrary
investor_guesses_sd = 5

#initializing
securities = {}
security_names = []

n_securities = 3 #I can choose this

#make a list of n securities
for i in range(n_securities):
    security_names.append(f"security{i}")

#use the list of n investor names as keys in the investors dictionary, with values that 
#are randomly generated estimates of security 1's fake value
for name in security_names:
    securities[name] = {"fake_value": random.randrange(0,100), #cap at 100 is arbitrary (should this be a normal distribution?)
                        "price": random.randrange(0,100)} #cap at 100 is arbitrary (should this be a normal distribution?)

print(securities)

#We have to do a for loop through the securities dictionary (this should be easier than for all the investors)
perfect_fv_investor = {}

for security in security_names:
     perfect_fv_investor[f"{security}_estimate"]  = securities[security]["fake_value"] 

print(perfect_fv_investor)

"""
#initializing
investors = {}
investor_names = []

n_investors = 5 #I can choose this

#make a list of n investor names
for i in range(n_investors):
    investor_names.append(f"investor{i}")

#use the list of n investor names as keys in the investors dictionary, with values that 
#are randomly generated estimates of security 1's fake value
for name in investor_names:
    investors[name] = {"security_1_estimate": np.random.normal(security_1["fake_value"],investor_guesses_sd)}
"""
    

""" If you want to test

print(f"Security 1: {security_1}")
print(f"Perfect Investor: {perfect_fv_investor}")
print(f"Investors: {investors}")
"""