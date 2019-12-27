from app.cards.cards import Card


class Player:
    def __init__(self, name):
        self._name = name
        self._hand = []
        self.score = 0

    def receive_card(self, card):
        self._hand.append(card)

    def get_hand(self):
        return self._hand

    def show_your_hand(self):
        for i in self._mao:
            print(self._mao[i])

    def show_your_score(self):
        return self.pontuacao

    def get_name(self):
        return self._name
