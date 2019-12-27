import unittest
from app.cards.cards import Card

class ReturnValue(unittest.TestCase):
    def setUp(self):
        self.card = Card(8,'Copas')

    def test_return_value_true(self):
        #   assert
        self.assertEqual(self.card._value ,8)

    def test_return_value_false(self):
        #   assert
        self.assertNotEqual(self.card._value,10)
    