```python

"""
Name: Ernest Hernandez
Email: ernest1721@yahoo.com 
Assignment: War Card Game
Due: 17 Feb 2017 @ 12:00 a.m.
"""

# -*- coding: utf-8 -*-

import os
import random
import time

CARD = """\
┌───────┐
│{}     │
│       │
│   {}  │
│       │
│     {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
┌───────┐
│{}    │
│       │
│   {}  │
│       │
│    {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

FACECARD = """\
┌───────┐
│{}│
│       │
│   {}  │
│       │
│{}│
└───────┘
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')

HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

class Card(object):
    
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]



        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14  
        }

        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,
        }

        self.suits = ['Spades','Hearts','Diamonds','Clubs']

        self.symbols = {
            'Spades':   '♠',
            'Diamonds': '♦',
            'Hearts':   '♥',
            'Clubs':    '♣',
        }


        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()
    

    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)
           
    def __cmp__(self,other):
        return self.points < other.points 
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

class Hand(list):
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []
    
    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
        
    def add(self,card):
        self._list.append(card)

    def sub_card(self):
        try:
            return self._list.pop(0)
        except IndexError:
            return print("Out of cards!")
        
    def sort(self):
        self._list = sorted(self._list)
        
    def __getitem__(self,key):
        return self._list[key]
        
class Game(object):
    def __init__(self):

        self.computer = {"name":"Computer","hand":Hand()}
        self.player = {"name":"Player","hand":Hand()}
        self.D = Deck()
        self.D.shuffle()
    
        for i in range(26):
            self.computer["hand"].add(self.D.pop_card())
            self.player["hand"].add(self.D.pop_card())

G1 = Game()

def play_war():
    #Creating variables for both players
    computer_hand = G1.computer["hand"]
    player_hand = G1.player["hand"]
    computer_pot = Hand()
    player_pot = Hand()
    win_pot = Hand()

    numplay = input("How many players are there? (1 or 2)\n")
    os.system('cls')

    if numplay == "1":
        #Do if only 1 player
        player_name = input("Please enter your name.\n")
        G1.player["name"] = player_name
        os.system('cls')
        computer_name = "Computer"
        G1.computer["name"] = computer_name
    elif numplay == "2":
        #Do if there are 2 players
        player_name = input("Please enter player 1's name.\n")
        G1.player["name"] = player_name
        os.system('cls')
        computer_name = input("Please enter player 2's name.\n")
        G1.computer["name"] = computer_name
        os.system('cls')

    print("""
                                Let the war begin!
                This is a simple game of war played by one or two players
                        Who ever has the higher value card wins!
       In the event of a tie, both will put 3 cards in a "Pot" and play the next round
    After each tie, both player pots will be displayed so you can see what's up for grabs
         The winner of each round collects both cards and all the cards in both pots
               The objective of the game is to get the entire deck of cards!
                                    Good luck!
    """)

    wait = input("Ok, press any key to begin!")
    os.system('cls')
    #Counter for number of draws
    round = 1

    #Do while both players have cards
    while computer_hand._list and player_hand._list:
        #Take the first card from player hands to display
        computer_card = computer_hand.sub_card()
        player_card = player_hand.sub_card()

        #Dislay player names and cards
        print()
        print("Round:", round)
        print()
        time.sleep(1)
        print(player_name)
        print(player_card)
        time.sleep(1.5)
        print()
        print(computer_name)
        print(computer_card)
        time.sleep(1)

        if computer_card.points == player_card.points:
            #Add displayed cards to both player pots
            computer_pot.add(computer_card)
            player_pot.add(player_card)
            
            for i in range(3):
                #Add the top 3 cards from both hands to their respective pots
                computer_pot.add(computer_hand.sub_card())
                player_pot.add(player_hand.sub_card())

            print("Its a DRAW! Both the played cards and 3 cards from both decks will be placed in the War Pot!\n")
            time.sleep(2.5)
            print(player_name + "'s Pot")
            print(player_pot)
            time.sleep(2.5)
            print("\n" + computer_name + "'s Pot")
            print(computer_pot)
            time.sleep(2.5)
            print()

        elif computer_card.points > player_card.points:
            #Distributes winning cards to the winner
            computer_pot.add(computer_card)
            player_pot.add(player_card)
            for i in range(len(computer_pot._list)):
                computer_hand.add(computer_pot.sub_card())
                computer_hand.add(player_pot.sub_card())
                
            print(G1.computer["name"], "wins that round!\n")
        
        elif computer_card.points < player_card.points:
            #Distributes winning cards to the winner
            computer_pot.add(computer_card)
            player_pot.add(player_card)
            for i in range(len(computer_pot._list)):
                player_hand.add(player_pot.sub_card())
                player_hand.add(computer_pot.sub_card())

            print(G1.player["name"], "wins that round!\n")
        
        #Displays the updated information on card locations after current round
        print(player_name + "'s Deck:", len(player_hand._list), computer_name + "'s Deck:", len(computer_hand._list),
        player_name + "'s Pot:", len(player_pot._list), computer_name + "'s Pot:", len(computer_pot._list), '\n')
        wait = input("Press 'Enter' to continue")
        os.system('cls')
        round += 1

    print()
    if computer_hand._list > player_hand._list:
        print(player_name + " has run out of cards, " + computer_name + " wins the war!\n")
    elif computer_hand._list < player_hand._list:
        print(computer_name + " has run out of cards, " + player_name + " wins the war!\n")
    else:
        print("It's a DRAW")
    
play_war()

```
