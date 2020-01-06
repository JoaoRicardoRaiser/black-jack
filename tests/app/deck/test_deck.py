import unittest
from unittest.mock import Mock

from app.deck.deck import Deck


class TestDeck(unittest.TestCase):

    def test_if_append_cards_in_deck_should_be_return_1(self):
        card_mock = Mock()
        deck = Deck()
        deck.append_cards_in_deck(card_mock)
        self.assertEqual(1, len(deck.get_deck()))

