# "Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would subclass the data
# structures to implement blackjack."
#
# I would have a deck object which contains four suit objects, and each suit object would contain 14 card objects.
# Each card object would have a face value, point vale, and suit. The deck object would have methods to shuffle.
# deal, and manipulate the cards.
#
# Player objects would have hand objects. The deck object would deal card objects from itself to the player hands.
# A table object would have "played" cards, played from player hands or the dealer (deck).
#
# The ace would require special handling since it can have two different point values at the player's discretion.
# Since this is the only exception, I would just have a special handler method for the ace.

# color styling the terminal output: https://gist.github.com/kamito/704813

import random
import time


def main():
    class Card:
        def __init__(self, face: str, point_value: int, suit: str):
            self.face = face
            self.point_value = point_value
            self.suit = suit
            self.face_up = False

    class Player:
        def __init__(self, name: str):
            self.name = name
            self.__hand = []
            self.score = None

        @property
        def hand(self) -> list:
            return self.__hand

        @hand.setter
        def hand(self, value: Card):
            self.__hand.append(value)



    class SuitOfCards:
        def __init__(self, suit: str):
            card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            self.suit = suit
            self.cards = []
            for face_name in card_list:
                if face_name.lower() in ["jack", "queen", "king"]:
                    point_value = 10
                elif face_name.lower() == "ace":
                    point_value = 1
                else:
                    point_value = int(face_name)
                card = Card(face_name, point_value, self.suit)
                self.add_card(card)

        def add_card(self, card):
            self.cards.append(card)

    class DeckOfCards:
        card_values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
                            "Queen": 10, "King": 10, "Ace": (1, 11)}

        def __init__(self, clubs: SuitOfCards = SuitOfCards("Clubs"),
                     diamonds: SuitOfCards = SuitOfCards("Diamonds"),
                     hearts: SuitOfCards = SuitOfCards("Hearts"),
                     spades: SuitOfCards = SuitOfCards("Spades")):
            self.clubs = clubs
            self.diamonds = diamonds
            self.hearts = hearts
            self.spades = spades
            self.cards = self.clubs.cards + self.spades.cards + self.hearts.cards + self.diamonds.cards
            self.blackjack_turn_number = 0

        def list_all_cards(self):
            for card in self.cards:
                time.sleep(.01)
                print(f"{card.face} of {card.suit}", end=", ")
            print("\r\n")

        def shuffle(self):
            random.shuffle(self.cards)
            print("The deck has been shuffled.\r\n")

        def start_game(self, game_name: str):
            if game_name.lower() == "blackjack":
                self.blackjack_turn_number = 0
            else:
                print("I am sorry, but I cannot play that game.")

        def blackjack_deal(self, player_list: list):
            self.blackjack_turn_number += 1
            for player in player_list:
                if player.name.lower() != "dealer" or self.blackjack_turn_number == 1:
                    self.cards[0].face_up = True
                player.hand.append(self.cards[0])
                self.cards.pop(0)
            if self.blackjack_turn_number == 1:
                print("\033[34m", end="")
                print("For the first deal...\r\n")
                print("\033[37m", end="")
            if self.blackjack_turn_number == 2:
                print("\033[34m", end="")
                print("For the second deal...\r\n")
                print("\033[37m", end="")
            print("\033[32m", end="")
            for player in player_list:
                for card in player.hand:
                    if card.face_up:

                        print(f"{player.name} has {card.face} of {card.suit}")
                    else:
                        print(f"{player.name} has 1 face down card.")
            print("\033[37m", end="")
            print("\r\n")

    print("Opening a new deck of cards!")
    deck_1 = DeckOfCards()
    print(".", end="")
    time.sleep(.4)
    print(".", end="")
    time.sleep(.4)
    print(".\r\n")
    time.sleep(.6)
    print("This deck has all the cards in it, go ahead see for yourself.\r\n")
    time.sleep(.2)
    deck_1.list_all_cards()
    time.sleep(.3)
    input("All good? <press any key to continue>\r\n")
    print("Now I'll shuffle the deck. Here is a peek.\r\n")
    deck_1.shuffle()
    deck_1.list_all_cards()
    time.sleep(.3)
    input("All good? <press any key to continue>\r\n")
    print("Now I have to shuffle it again. This time no peeking!\r\n")
    deck_1.shuffle()
    player_name = input("We can play blackjack now. What is your name?\r\n")
    time.sleep(.3)
    dealer_player = Player("Dealer")
    player_1 = Player(player_name)
    print(f"Okay, {player_1.name}, let us begin.\r\n")
    time.sleep(.3)
    print("First, we'll deal you a card.\r\n")
    time.sleep(.3)
    deck_1.blackjack_deal([dealer_player, player_1])
    time.sleep(.7)
    deck_1.blackjack_deal([dealer_player, player_1])


main()
