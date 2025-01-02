# Symbols and spin row
import random

# Define symbols for the sloat machines
def spin_row():
    
    # Define the symbos for the slot machine
    symbols = ["🍒", "🍋", "🍊", "🍇", "🍉"]
    
    #Return a random symbol from the list
    return [random.choice(symbols) for _ in range(3)]

# Test the spin_row function
#print(spin_row())

# Display the row of symbols 
def display_spin(spin):
    
    print("**************")
    print(" | ".join(spin))
    print("**************")


# Test the display_spin function    
"""print("Testing display_spin : ")
test_row = ['🍒', '🍉', '🍋']
display_spin(test_row)
"""
# calculate the payout for the spin
def get_payout(row, bet):
    
    # check if all symbols are the same 
    if row[0] == row[1] == row[2]:
        if row [0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🍊":
            return bet * 5
        elif row[0] == "🍇":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 20
    return 0
# Test the get_payout function
"""print("Testing get_payout :")
test_row = ['🍒', '🍒', '🍒']
print(test_row, get_payout(test_row, 10))    
    """

# Game logic 
# Game logic
def main():
    initial_balance = 100
    print("**************************")
    print("Welcome to the python slots")
    print("Symbols: 🍒 🍋 🍊 🍇 🍉")
    print("**************************")

    while initial_balance > 0:
        print(f"Current Balance: ${initial_balance}")
        
        # Get the bet amount as a string for validation
        bet_input = input("Enter your bet amount: ")
        
        # Validate the input to ensure it's a valid number
        if not bet_input.isdigit():
            print("Please enter a valid number")
            continue
        
        # Convert valid input to an integer
        bet = int(bet_input)
        
        # Check if the bet is within the balance
        if bet > initial_balance:
            print("Insufficient balance")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        # Deduct the bet amount from the balance
        initial_balance -= bet
        row = spin_row()
        print("Spinning the slot machine.....")
        display_spin(row)
        
        # Calculate the payout
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"Congratulations! You won ${payout}")
        else:
            print("Sorry! You lost this game")
        
        # Add the payout to the balance
        initial_balance += payout
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again != "yes":
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${initial_balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()
