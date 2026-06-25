"""
Program Name: Lab9_username-1.py
Author: Hriday Vermani
Purpose: Main game file that manages the game loop, coin matching rules, and user interaction.
Starter Code: None 
Date: June 24 2026
"""
from player import Player

def main():
    print("--- Coin Match Game ---")
    
    # Initialize the two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Show initial balances
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")
    
    # Prompt user for the first round
    keep_playing = input("Do you want to toss the coins? (y/n): ").lower()
    
    while keep_playing == 'y':
        print("\nTossing...")
        
        # Force players to toss their respective coins
        player1.toss_coin()
        player2.toss_coin()
        # Get the results of the toss
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")
        
        # Game Rules Logic
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"...It's a Match! {player1.get_name()} wins a coin.\n")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"...No Match! {player2.get_name()} wins a coin.\n")
            
        # Report current scores
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")