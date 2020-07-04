import random

import Player
from Deck import Deck
from const import MESSAGES

class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        while True:
            bots_qty = int(
            input("Hey, how many players do you want to play a game? "))
            if bots_qty <= self.max_pl_count - 1:
                break
        self.all_players_count = bots_qty + 1

        for i in range(bots_qty):
            # todo: should be random pos
            b = Player.Bot(position=i)
            self.players.append(b)
            print(b, ' is created')
        self.player = Player.Player(position=bots_qty + 1)
        self.players.append(self.player)

    def ask_bets(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)


    def first_desc(self):
        for player in self.players:
            player.ask_card(self.deck, 2)

    def start(self):
        # todo: max players count?
        if not self._ask_starting(MESSAGES.get('ask_start')):
            exit(1)

        self._launching()
        self.ask_bets()
        self.first_desc()
