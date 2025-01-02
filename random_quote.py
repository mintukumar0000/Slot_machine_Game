"""from quote import quote
import random

quotes = quote(input("Enter the name of your favorite author: "))
print(random.choice(quotes)['quote'] if quotes else "No quotes found!")# random.choice is used for choosing the random quotes from the quote
"""
from quote import quote 
import random

quotes = quote(input("Enter the name of your favorite author/person: "))
print(random.choice(quotes)['quote'] if quotes else "No quotes found!")