import unittest
from app.cards.cards import Card

class TestInstance(unittest.TestCase):
    def setUp(self):
        self.card = Card(4,'Paus')

    def test_instance_card_true(self):
        #   assert
        assert isinstance(self.card,Card) == True
        self.assertIsInstance(self.card,Card)

    def test_instance_card_false(self):
        #   assert
        assert isinstance(self.card,TestInstance) == False