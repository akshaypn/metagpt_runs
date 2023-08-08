from art import *
from pyfiglet import Figlet


class ASCIIArt:
    @staticmethod
    def get_welcome_message() -> str:
        """
        Get the ASCII art for the welcome message.

        Returns:
            str: The ASCII art for the welcome message.
        """
        return text2art("Welcome to Blackjack!")

    @staticmethod
    def get_card_art(rank: str, suit: str) -> str:
        """
        Get the ASCII art for a card.

        Args:
            rank (str): The rank of the card.
            suit (str): The suit of the card.

        Returns:
            str: The ASCII art for the card.
        """
        card_art = Figlet(font="slant")
        return card_art.renderText(f"{rank} {suit}")
