from typing import List
from deck import Deck
from player import Player
from dealer import Dealer
from utils import format_currency


class Game:
    def __init__(self):
        self.player = Player("Player", 100)
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet = 0
        self.winnings = 0

    def start_game(self):
        """
        Start a new game.
        """
        self.deck.shuffle()
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.bet = 0
        self.winnings = 0

    def place_bet(self, amount: int):
        """
        Place a bet.

        Args:
            amount (int): The amount to bet.
        """
        self.bet = amount
        self.player.remove_chips(amount)

    def deal_initial_cards(self):
        """
        Deal the initial cards to the player and the dealer.
        """
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def player_hit(self):
        """
        Player chooses to hit and receives another card.
        """
        self.player.add_card(self.deck.deal_card())

    def player_stand(self):
        """
        Player chooses to stand and ends their turn.
        """
        pass

    def dealer_hit(self):
        """
        Dealer hits for another card.
        """
        if self.dealer.hand.get_value() < 17:
            self.dealer.add_card(self.deck.deal_card())

    def determine_winner(self):
        """
        Determine the winner of the game.
        """
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        if player_value > 21:
            self.winnings -= self.bet
        elif dealer_value > 21:
            self.winnings += self.bet
        elif player_value > dealer_value:
            self.winnings += self.bet
        elif player_value < dealer_value:
            self.winnings -= self.bet

        self.player.add_chips(self.winnings)

    def end_game(self):
        """
        End the game and display the outcome.
        """
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        print("Player's hand:", self.player.hand.cards)
        print("Dealer's hand:", self.dealer.hand.cards)

        print("Player's hand value:", player_value)
        print("Dealer's hand value:", dealer_value)

        if player_value > 21:
            print("Player busts! You lose.")
        elif dealer_value > 21:
            print("Dealer busts! You win.")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose.")
        else:
            print("It's a tie.")

        print("Total winnings:", format_currency(self.winnings))
