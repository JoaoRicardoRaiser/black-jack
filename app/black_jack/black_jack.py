from app.dealer.dealer import Dealer
from app.jogador.player import Player


class BlackJack:
    def __init__(self, player: Player, dealer: Dealer):
        self._player = player
        self._dealer = dealer

    def welcome_mensage(self):
        print("=" * 60)
        print(f"Seja bem vindo ao Black Jack {self._player.get_name()} !!!")
        print("=" * 60)

    def dealer_delivering_card(self):
        return self._player.receive_card(self._dealer.get_card())


    def score_player(self):
        for card in self._player.get_hand():
            if (card._value == 'Q'
                    or card._value == 'J'
                    or card._value == 'K'):
                self._player.score += 10
            else:
                self._player.score += card.get_value()
        return print(f'Sua pontuação é: {self._player.score}')

    def check_status_game(self):
        if self._player.score > 21:
            print('Perdeu !!!!!')

        if self._player.score == 21:
            print('Você ganhou !!!!')


    def dealer_quest(self):
        return self._dealer.want_continue()

    def check_cards(self):
        for i in self._player.get_hand():
            print(f'A carta retirada foi: {i.get_name()}')

    def check_quantity_cards(self):
        print(f"Ainda restam {len(self._dealer.get_deck())} cartas no baralho")




