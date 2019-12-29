import unittest

from app.cards.cards import Card


class TestCards(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card(5, '5 de Paus')

    def test_get_name_card(self):
        self.assertEqual(self.card.get_name(), '5 de Paus')

    def test_get_value_card(self):
        self.assertEqual(self.card.get_value(), 5)
