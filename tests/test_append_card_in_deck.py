import unittest
from app.cards.cards import Card
from app.deck.deck import Deck


class TestAppend(unittest.TestCase):

    def setUp(self):
        self.card = Card(7,'Copas')
        self.deck = Deck()

    def test_append_true(self):
        #   action
        self.deck.append_cards_in_deck(self.card)

        #   assert
        assert len(self.deck.cards) == 1

    def test_append_false(self):
        #   action
        self.deck.append_cards_in_deck('a')

        #   assert
        assert len(self.deck.cards) == 1