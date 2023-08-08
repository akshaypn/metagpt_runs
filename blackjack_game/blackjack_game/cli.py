import click
from tabulate import tabulate
from colorama import Fore, Style
from game import Game
from ascii_art import ASCIIArt
from utils import format_currency


class CLI:
    def __init__(self):
        self.game = Game()

    def start(self):
        self.print_welcome_message()
        self.print_instructions()
        self.get_user_input()

    def print_welcome_message(self):
        welcome_message = ASCIIArt.get_welcome_message()
        print(welcome_message)

    def print_instructions(self):
        print("Instructions:")
        print("- Start a new game by typing 'start'")
        print("- Place a bet by typing 'bet <amount>'")
        print("- Hit for another card by typing 'hit'")
        print("- Stand and end your turn by typing 'stand'")
        print("- Quit the game by typing 'quit'")

    def print_current_hand(self):
        player_hand = self.game.player.hand.cards
        dealer_hand = self.game.dealer.hand.cards

        player_hand_table = [[card.rank, card.suit] for card in player_hand]
        dealer_hand_table = [[card.rank, card.suit] for card in dealer_hand]

        print("Your hand:")
        print(tabulate(player_hand_table, headers=["Rank", "Suit"], tablefmt="fancy_grid"))
        print("Dealer's hand:")
        print(tabulate(dealer_hand_table, headers=["Rank", "Suit"], tablefmt="fancy_grid"))

    def print_dealer_hand(self):
        dealer_hand = self.game.dealer.hand.cards

        dealer_hand_table = [[card.rank, card.suit] for card in dealer_hand]

        print("Dealer's hand:")
        print(tabulate(dealer_hand_table, headers=["Rank", "Suit"], tablefmt="fancy_grid"))

    def print_outcome(self):
        player_value = self.game.player.hand.get_value()
        dealer_value = self.game.dealer.hand.get_value()

        print("Player's hand value:", player_value)
        print("Dealer's hand value:", dealer_value)

        if player_value > 21:
            print(Fore.RED + "Player busts! You lose." + Style.RESET_ALL)
        elif dealer_value > 21:
            print(Fore.GREEN + "Dealer busts! You win." + Style.RESET_ALL)
        elif player_value > dealer_value:
            print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        elif player_value < dealer_value:
            print(Fore.RED + "You lose." + Style.RESET_ALL)
        else:
            print("It's a tie.")

    def print_total_winnings(self):
        total_winnings = self.game.player.chips
        print("Total winnings:", format_currency(total_winnings))

    def print_quit_message(self):
        print("Thank you for playing! Goodbye.")

    def get_user_input(self):
        while True:
            user_input = input("Enter a command: ")

            if user_input == "start":
                self.game.start_game()
                self.print_current_hand()
            elif user_input.startswith("bet"):
                try:
                    amount = int(user_input.split()[1])
                    self.game.place_bet(amount)
                    self.print_current_hand()
                except (IndexError, ValueError):
                    print("Invalid command. Please enter a valid bet amount.")
            elif user_input == "hit":
                self.game.player_hit()
                self.print_current_hand()
                if self.game.player.hand.get_value() > 21:
                    self.print_outcome()
                    self.print_total_winnings()
                    self.get_user_input()
            elif user_input == "stand":
                self.game.player_stand()
                self.print_dealer_hand()
                while self.game.dealer.hand.get_value() < 17:
                    self.game.dealer_hit()
                    self.print_dealer_hand()
                self.game.determine_winner()
                self.print_outcome()
                self.print_total_winnings()
                self.get_user_input()
            elif user_input == "quit":
                self.print_quit_message()
                break
            else:
                print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":
    cli = CLI()
    cli.start()
