import unittest
from unittest.mock import patch, MagicMock, Mock, call

from app.cards.cards import Card
from app.dealer.dealer import Dealer


class TestDealer(unittest.TestCase):

    def setUp(self) -> None:
        self.dealer = Dealer()

    @patch('app.dealer.dealer.Card')
    def test_create_black_jack_deck(self, mock_card):
        dealer = Dealer()
        dealer.deck_black_jack()
        assert mock_card.mock_calls == [
            call(1, '1 de Paus'),
            call(1, '1 de Copas'),
            call(1, '1 de Espadas'),
            call(1, '1 de Ouros'),
            call(2, '2 de Paus'),
            call(2, '2 de Copas'),
            call(2, '2 de Espadas'),
            call(2, '2 de Ouros'),
            call(3, '3 de Paus'),
            call(3, '3 de Copas'),
            call(3, '3 de Espadas'),
            call(3, '3 de Ouros'),
            call(4, '4 de Paus'),
            call(4, '4 de Copas'),
            call(4, '4 de Espadas'),
            call(4, '4 de Ouros'),
            call(5, '5 de Paus'),
            call(5, '5 de Copas'),
            call(5, '5 de Espadas'),
            call(5, '5 de Ouros'),
            call(6, '6 de Paus'),
            call(6, '6 de Copas'),
            call(6, '6 de Espadas'),
            call(6, '6 de Ouros'),
            call(7, '7 de Paus'),
            call(7, '7 de Copas'),
            call(7, '7 de Espadas'),
            call(7, '7 de Ouros'),
            call(8, '8 de Paus'),
            call(8, '8 de Copas'),
            call(8, '8 de Espadas'),
            call(8, '8 de Ouros'),
            call(9, '9 de Paus'),
            call(9, '9 de Copas'),
            call(9, '9 de Espadas'),
            call(9, '9 de Ouros'),
            call(10, '10 de Paus'),
            call(10, '10 de Copas'),
            call(10, '10 de Espadas'),
            call(10, '10 de Ouros'),
            call('Q', 'Q de Paus'),
            call('Q', 'Q de Copas'),
            call('Q', 'Q de Espadas'),
            call('Q', 'Q de Ouros'),
            call('J', 'J de Paus'),
            call('J', 'J de Copas'),
            call('J', 'J de Espadas'),
            call('J', 'J de Ouros'),
            call('K', 'K de Paus'),
            call('K', 'K de Copas'),
            call('K', 'K de Espadas'),
            call('K', 'K de Ouros'),
            call(1, '1 de Paus'),
            call(1, '1 de Copas'),
            call(1, '1 de Espadas'),
            call(1, '1 de Ouros'),
            call(2, '2 de Paus'),
            call(2, '2 de Copas'),
            call(2, '2 de Espadas'),
            call(2, '2 de Ouros'),
            call(3, '3 de Paus'),
            call(3, '3 de Copas'),
            call(3, '3 de Espadas'),
            call(3, '3 de Ouros'),
            call(4, '4 de Paus'),
            call(4, '4 de Copas'),
            call(4, '4 de Espadas'),
            call(4, '4 de Ouros'),
            call(5, '5 de Paus'),
            call(5, '5 de Copas'),
            call(5, '5 de Espadas'),
            call(5, '5 de Ouros'),
            call(6, '6 de Paus'),
            call(6, '6 de Copas'),
            call(6, '6 de Espadas'),
            call(6, '6 de Ouros'),
            call(7, '7 de Paus'),
            call(7, '7 de Copas'),
            call(7, '7 de Espadas'),
            call(7, '7 de Ouros'),
            call(8, '8 de Paus'),
            call(8, '8 de Copas'),
            call(8, '8 de Espadas'),
            call(8, '8 de Ouros'),
            call(9, '9 de Paus'),
            call(9, '9 de Copas'),
            call(9, '9 de Espadas'),
            call(9, '9 de Ouros'),
            call(10, '10 de Paus'),
            call(10, '10 de Copas'),
            call(10, '10 de Espadas'),
            call(10, '10 de Ouros'),
            call('Q', 'Q de Paus'),
            call('Q', 'Q de Copas'),
            call('Q', 'Q de Espadas'),
            call('Q', 'Q de Ouros'),
            call('J', 'J de Paus'),
            call('J', 'J de Copas'),
            call('J', 'J de Espadas'),
            call('J', 'J de Ouros'),
            call('K', 'K de Paus'),
            call('K', 'K de Copas'),
            call('K', 'K de Espadas'),
            call('K', 'K de Ouros')
        ]

    @patch('app.dealer.dealer.random')
    def test_if_dealer_gets_card_from_deck(self, random_mock):
        dealer = Dealer()
        dealer._deck = ["5 de copas", '3 de copas']
        selected_card = dealer.get_card_from_deck()
        self.assertEqual("5 de copas", selected_card)
        random_mock.shuffle.assert_called_once()


    @patch('app.dealer.dealer.input')
    def test_want_continue_not(self, mock_input):
        player_mock = MagicMock()
        player_mock.you_have_cards_in_hand = MagicMock(return_value=False)
        mock_input.return_value = "N"
        dealer = Dealer()
        self.assertFalse(dealer.want_continue(player_mock))
        mock_input.assert_called_once_with('Quer retirar uma carta? S/N\n')

    @patch('app.dealer.dealer.input')
    def test_want_continue_yes(self, mock_input):
        mock_player = MagicMock()
        mock_player.you_have_cards_in_hand = MagicMock(return_value = True)
        mock_input.return_value = "S"
        dealer = Dealer()
        self.assertTrue(dealer.want_continue(mock_player))
        mock_input.assert_called_once_with('Quer uma nova carta? S/N\n')


    @patch('app.dealer.dealer.Card')
    def test_should_remove_card_from_deck(self, card_mock):

        card_mock = MagicMock(return_value='1 de Paus')
        dealer = Dealer()
        dealer._deck = ['1 de copas', '2 de Copas']
        dealer.remove_card_from_deck(card_mock)
        self.assertEqual(['2 de Copas'], dealer._deck)

