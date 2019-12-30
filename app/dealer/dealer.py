import random
from app.cards.cards import Card
from app.player.player import Player


class Dealer:
    def __init__(self):
        self._deck = self.deck_black_jack()

    @staticmethod
    def deck_black_jack():
        black_jack_deck = []
        value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
        suit_list = ['Paus', 'Copas', 'Espadas', 'Ouros']
        for i in range(len(value_list)):
            for j in range(len(suit_list)):
                card = Card(value_list[i], f'{value_list[i]} de {suit_list[j]}')
                black_jack_deck.append(card)
        return black_jack_deck

    def want_continue(self, player: Player) -> bool:
        if not player.you_have_cards_in_hand():
            answer = input("Quer retirar uma carta? S/N\n")
        else:
            answer = input("Quer uma nova carta? S/N\n")
        if answer == 'S' or answer == 's':
            return True
        return False

    def get_card_from_deck(self):
        random.shuffle(self._deck)
        return self._deck[0]

    def remove_card_from_deck(self, card: Card):
        self._deck.remove(card)


    def get_deck(self):
        return self._deck

