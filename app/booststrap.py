from app.black_jack.black_jack import BlackJack
from app.dealer.dealer import Dealer
from app.player.player import Player


def instance_all():
    player = Player(input("Meu caro, digite seu nome: "))
    dealer = Dealer()
    object_black_jack = BlackJack(player, dealer)
    return object_black_jack


class Start:

    @staticmethod
    def execute():
        black_jack = instance_all()

        black_jack.welcome_message()
        while black_jack.quantity_cards() != 0:
            if black_jack.check_if_has_result():
                break
            if black_jack.dealer_quest():
                black_jack.dealer_delivering_card()
                black_jack.show_quantity_cards()
                black_jack.show_cards_in_hand_player()
                black_jack.show_score_player()
            else:
                break



        black_jack.farewell_message(black_jack)
