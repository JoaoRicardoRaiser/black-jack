from app.cards.cards import Card


class Player:
    def __init__(self, name):
        self._name = name
        self._hand = []
        self.score = 0

    def receive_card(self, card: Card):
        self._hand.append(card)

    def get_hand(self):
        return self._hand

    def show_your_score(self):
        return self.score

    def get_name(self):
        return self._name

    def you_have_cards_in_hand(self):
        if self._hand:
            return True
        return False


