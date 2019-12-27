import unittest
from app.dealer.dealer import Dealer
from app.black_jack.black_jack import BlackJack

class TestAppend(unittest.TestCase):

    def setUp(self):
        self.baralho = BlackJack().black_jack_deck()
        self.dealer = Dealer(self.baralho[:])

    def test_shuffle_deck(self):
        #   assert
        self.dealer.shuffle()
        self.assertNotEqual(self.dealer._baralho, self.baralho)