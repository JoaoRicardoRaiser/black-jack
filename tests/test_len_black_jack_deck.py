import unittest
from app.black_jack.black_jack import BlackJack

class TestLenBlackJackDeck(unittest.TestCase):
    def setUp(self):
        self.black_jack = BlackJack().black_jack_deck()

    def test_len_black_jack_deck(self):
        
        #   arrange
        assert len(self.black_jack) == 52
