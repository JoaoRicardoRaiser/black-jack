from app.cards.cards import Card


class Deck:

    def __init__(self):
        self._cards = []

    def append_cards_in_deck(self, card: Card):
        self._cards.append(card)

    def get_deck(self):
        return self._cards
