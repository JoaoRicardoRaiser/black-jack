from app.cards.cards import Card


class Deck:

    def __init__(self):
        self.cards = []

    def append_cards_in_deck(self, card: Card):
        self.cards.append(card)
