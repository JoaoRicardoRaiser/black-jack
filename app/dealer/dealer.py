import random
from app.cards.cards import Card


class Dealer:
    def __init__(self):
        self._deck = self.deck_black_jack(self)

    @staticmethod
    def deck_black_jack(self):
        black_jack_deck = []
        value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
        suit_list = ['Paus', 'Copas', 'Espadas', 'Ouros']
        for i in range(len(value_list)):
            for j in range(len(suit_list)):
                card = Card(value_list[i], f'{value_list[i]} de {suit_list[j]}')
                black_jack_deck.append(card)
        return black_jack_deck


    def want_continue(self):
        answer = input("Você ainda quer jogar? S/N\n")
        if answer == 'S' or answer == 's':
            return True

    def shuffle(self):
        random.shuffle(self._deck)

    def get_card(self):
        self.shuffle()
        selected_card = random.choice(self._deck)
        self._deck.remove(selected_card)
        return selected_card

        #JOGAO
        # self.shuffle()
        # selected_card = random.choice(self._deck())
        # self._deck.remove(selected_card)
        # return selected_card

    def get_deck(self):
        return self._deck

