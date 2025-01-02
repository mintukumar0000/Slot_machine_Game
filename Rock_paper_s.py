import sys

user1 = input("What's your name? ")
user2 = input("And, your's name plz? ")

user1_ans= input("%s, do you want to choose rock, paper or scissor?" % user1)
user2_ans= input("%s, do you want to choose rock, paper or scissor?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tied!")
    elif u1 == 'rock':
        if u2 == 'scissor':
            return("Rock's wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissor':
        if u2 == 'paper':
            return("Scissor wins!")
        else:
            return("Rock's wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")
    else:
        return("Invalid input, please try again")
    sys.exit()

print(compare(user1_ans, user2_ans))
                