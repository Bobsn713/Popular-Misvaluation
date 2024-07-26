import random
import numpy as np

#5 is arbitrary
investor_guesses_sd = 5

security_1 = {
    "fake_value" : random.randrange(0,100), #cap at 100 is arbitrary (should this be a normal distribution?),
    "price" : random.randrange(0,100), #cap at 100 is arbitrary (should this be a normal distribution?)
}

perfect_fv_investor = {
    "security_1_estimate" : security_1["fake_value"]

}

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
    investors[name] = {"security_1_estimate": np.random.normal(security_1["fake_value"],investor_guesses_sd)} #the[0] is because it returns as an array and I don't want an array

""" If you want to test

print(f"Security 1: {security_1}")
print(f"Perfect Investor: {perfect_fv_investor}")
print(f"Investors: {investors}")
"""