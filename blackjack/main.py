from Deck import Deck
from Game import Game

if __name__ == '__main__':
    """ d = Deck()
    print(len(d))
    c = d.get_card()
    print(c)
    print(len(d) """

    g = Game()
    g.start()

    for pl in g.players:
        pl.print_cards()
        print('*'*12)