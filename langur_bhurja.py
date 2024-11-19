#DICE ROLLING GAME (Langur Bhurja)

#----------------------------------------

import random

def roll_dice():
    """Simulate rolling a single die with six symbols."""
    return random.choice(['club', 'spade', 'heart', 'diamond', 'crown', 'flag'])

def calculate_winnings(bet_amount, matches):
    """Calculate winnings based on the number of matches for a symbol."""
    if matches == 1 or matches == 0:
        return 0
    else:
        return bet_amount * matches + bet_amount

def main():
    print("Welcome to the Dice Betting Game!")
    symbols = ['club', 'spade', 'heart', 'diamond', 'crown', 'flag']
    
    # Prompt user for symbols and bets
    chosen_symbols = input("Enter the symbols you'd like to bet on (space-separated from 'club', 'spade', 'heart', 'diamond', 'crown', 'flag'): ").split()
    chosen_symbols = [symbol for symbol in chosen_symbols if symbol in symbols]
    if not chosen_symbols:
        print("You must choose at least one valid symbol to bet on.")
        return
    
    # Get individual bet amounts for each chosen symbol
    bet_amounts = {}
    for symbol in chosen_symbols:
        while True:
            try:
                amount = float(input(f"Enter your bet amount for '{symbol}': $"))
                if amount <= 0:
                    print("Bet amount must be greater than zero.")
                else:
                    bet_amounts[symbol] = amount
                    break
            except ValueError:
                print("Please enter a valid number.")

    # Roll the dice 6 times
    rolls = [roll_dice() for _ in range(6)]
    print("\nRolling six dice...")
    print(f"The dice rolled: {rolls}")
    
    # Count occurrences of each chosen symbol in the roll results
    winnings = 0
    for symbol in chosen_symbols:
        matches = rolls.count(symbol)
        win_amount = calculate_winnings(bet_amounts[symbol], matches)
        winnings += win_amount
        print(f"- You chose '{symbol}': matched {matches} times, winning ${win_amount:.2f}")
    
    # Display total winnings and game result
    print(f"\nTotal winnings: ${winnings:.2f}")
    if winnings > sum(bet_amounts.values()):
        print("Congratulations! You won more than your total bet!")
    elif winnings == sum(bet_amounts.values()):
        print("You broke even. No loss, no gain!")
    else:
        print("You lost this round. Better luck next time!")
    
    # Ask if the player wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
main()