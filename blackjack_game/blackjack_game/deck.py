from typing import List
import random


class Card:
    def __init__(self, value: int, suit: str, rank: str):
        self.value = value
        self.suit = suit
        self.rank = rank


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(value, suit, rank) for suit in suits for value, rank in enumerate(ranks, start=1)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()
