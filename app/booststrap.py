from app.black_jack.black_jack import BlackJack
from app.dealer.dealer import Dealer
from app.player.player import Player

class Start:

    def execute(self):
        player = Player(input("Meu caro, digite seu nome: "))
        dealer = Dealer()

        black_jack = BlackJack(player, dealer)

        black_jack.welcome_mensage()

        while black_jack.quantity_cards() != 0:
            if black_jack.dealer_quest():
                black_jack.dealer_delivering_card()
                black_jack.show_quantity_cards()
                black_jack.show_cards_in_hand_player()
                black_jack.show_score_player()
            else:
                break

        print(("="*60),)
        black_jack.check_result()
        print(("="*60),)
        print('Obrigado por utilizar este produto')
        print(("="*60))