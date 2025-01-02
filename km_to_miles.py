import math

def km_to_miles(kms):
    miles = kms * 0.62137
    return miles

# To test 
kms = 10
miles = km_to_miles(kms)
print(f"{kms} kilometers is equal to {miles} miles.")