import random
import numpy as np

n_investors_input = ["investor1", "investor2", "investor3"]  #can change to what I want


#defining this outside the dictionary because the "price" has to reference it and can't be self referencing (I think)
sec1_fv = random.randrange(0,100), #cap at 100 is arbitrary (should this be a normal distribution?)

security_1 = {
    "fake_value" : sec1_fv,
    "price" : sec1_fv
}

perfect_fv_investor = {
    "security_1_estimate" : security_1["fake_value"]

}

#generating other investors (This doesn't work)
#def make_investors(n_investors):
#    for i in n_investors:
#        i = {
#            "security_1_estimate" : np.random.normal(security_1["fake_value"],5) #std dev of 5 is arbitrary
#        }

investor1 = {
    "security_1_estimate" : np.random.normal(security_1["fake_value"],5) #std dev of 5 is arbitrary
}

investor2 = {
    "security_1_estimate" : np.random.normal(security_1["fake_value"],5) #std dev of 5 is arbitrary
}

investor3 = {
    "security_1_estimate" : np.random.normal(security_1["fake_value"],5) #std dev of 5 is arbitrary
}

#running it
#make_investors(n_investors_input)

print("Security 1", security_1)
print("Investor 1",  investor1)
print("Investor 2", investor2)
print("Investor 3", investor3)
print("Perfect Investor", perfect_fv_investor)
