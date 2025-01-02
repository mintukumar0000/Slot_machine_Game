#Import module 
import random
import string

# Store all the character in the string 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# ask user to input their number of charactes
uer_input = input("How many charactes do you want in your password? ")

# if the chacters is less then 8
while True:
 
    try:
 
        characters_num = int(user_input)
 
        if characters_num < 8:
 
            print("Your number should be at least 8.")
 
            user_input = input("Please, Enter your number again: ")
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only.")
 
        user_input = input("How many characters do you want in your password? ")

# suffle all the list
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate 30% and 20% of the charactes in the numbers
part1 = round(characters_num * 30/100)
part2 = round(characters_num * 20/100)

# Generate the number of charactes (60% charactes and 40% digits and punctuations)
result = []

for x in range(part1):

    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):

    result.append(s3[x])
    result.append(s4[x])

# suffle the result
random.shuffle(result)

# join the reslut 
password = "".join(result)
print("Strong password:", password)