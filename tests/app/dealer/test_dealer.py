import unittest
from unittest.mock import patch

from app.dealer.dealer import Dealer


class TestDealer(unittest.TestCase):

    def setUp(self) -> None:
        self.dealer = Dealer()

    def test_create_black_jack_deck_check_names(self):
        created_deck = self.dealer.deck_black_jack()
        list_created_deck_with_name_cards = []
        list_dealer_deck_names = []
        for card in created_deck:
            list_created_deck_with_name_cards.append(card.get_name())

        for card in self.dealer._deck:
            list_dealer_deck_names.append(card.get_name())

        self.assertEqual(list_created_deck_with_name_cards, list_dealer_deck_names)

    def test_create_black_jack_deck_check_values(self):
        created_deck = self.dealer.deck_black_jack()
        list_created_deck_with_value_cards = []
        list_dealer_deck_value = []
        for card in created_deck:
            list_created_deck_with_value_cards.append(card.get_value())

        for card in self.dealer._deck:
            list_dealer_deck_value.append(card.get_value())

        self.assertEqual(list_created_deck_with_value_cards, list_dealer_deck_value)

    @patch('app.dealer.dealer.Dealer.want_continue')
    def test_function_want_continue(self, mock_answer):
        mock_answer.return_value.answer.return_value = 's'
        self.assertEqual(mock_answer.return_value, True)

