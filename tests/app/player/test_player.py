import unittest
from unittest.mock import Mock

from app.cards.cards import Card
from app.player.player import Player


class TestPlayer(unittest.TestCase):

    def test_if_player_receive_card_should_append_in_your_hand(self):
        card_mock = 1
        player = Player('João')
        player.receive_card(card_mock)
        self.assertEqual(len(player.get_hand()), 1)

    def test_if_player_have_cards_on_hand_should_be_return_true(self):
        card_mock = Mock()
        player = Player('João')
        player.receive_card(card_mock)
        self.assertTrue(player.you_have_cards_in_hand())

    def test_if_player_have_cards_on_hand_should_be_return_false(self):
        player = Player('João')
        self.assertFalse(player.you_have_cards_in_hand())


