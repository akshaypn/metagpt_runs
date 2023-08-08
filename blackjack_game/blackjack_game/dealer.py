from typing import List

class Card:
    def __init__(self, value: int, suit: str, rank: str):
        self.value = value
        self.suit = suit
        self.rank = rank

class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self) -> int:
        """
        Get the value of the hand.

        Returns:
            int: The value of the hand.
        """
        value = 0
        num_aces = 0

        for card in self.cards:
            value += card.value

            if card.rank == "Ace":
                num_aces += 1

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def add_card(self, card: Card):
        """
        Add a card to the hand.

        Args:
            card (Card): The card to add to the hand.
        """
        self.cards.append(card)

    def clear(self):
        """
        Clear the hand.
        """
        self.cards = []

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def add_card(self, card: Card):
        """
        Add a card to the dealer's hand.

        Args:
            card (Card): The card to add to the hand.
        """
        self.hand.add_card(card)

    def clear_hand(self):
        """
        Clear the dealer's hand.
        """
        self.hand.clear()
