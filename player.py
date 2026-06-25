"""
Program Name: player.py
Author: Hriday Vermani
Purpose: Represents a player who has a name, a wallet, and an instance of a Coin object.
Starter Code: None 
Date: June 24 2026

"""

from coin import Coin

class Player:
    def __init__(self, name: str) -> None:
        """Initializes the player with a name, a wallet balance of 20, and a Coin object."""
        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin()

    def toss_coin(self) -> None:
        """Tells the player's coin to toss itself."""
        self.__coin.toss()

    def get_coin_side(self) -> str:
        """Gets the side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self) -> None:
        """Adds 1 coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self) -> None:
        """Subtracts 1 coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self) -> int:
        """Returns the current value of the player's wallet."""
        return self.__wallet

    def get_name(self) -> str:
        """Returns the player's name."""
        return self.__name
    