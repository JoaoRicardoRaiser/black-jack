from app.cards.cards import Card
from app.dealer.dealer import Dealer
from app.player.player import Player


class BlackJack:
    def __init__(self, player: Player, dealer: Dealer):
        self._player = player
        self._dealer = dealer

    def welcome_mensage(self):
        print("=" * 60)
        print(f"Seja bem vindo ao Black Jack {self._player.get_name()} !!!")
        print("=" * 60)

    def dealer_delivering_card(self):
        selected_card = self._dealer.get_card_from_deck()
        self.addict_score_player(selected_card)
        self._player.receive_card(selected_card)
        self._dealer.remove_card_from_deck(selected_card)
        return self.show_retired_card(selected_card)


    def addict_score_player(self, card: Card):
        if (card._value == 'Q'
                or card._value == 'J'
                or card._value == 'K'):
            self._player.score += 10
        else:
            self._player.score += card.get_value()

    def check_result(self):
        if self._player.score > 21:
            print('Resultado: Puxa vida, você perdeu\n'
                  'Tente novamente')
        elif self._player.score == 21:
            print('Resultado: Você ganhou !\n'
                  'Parabéns !')
        else:
            print('Resultado: Não houve resultado\n'
                  ' :( ')

    def dealer_quest(self):
        return self._dealer.want_continue(self._player.get_hand())

    def show_retired_card(self, card: Card):
            print(f'A carta retirada foi: {card.get_name()}')

    def show_score_player(self):
        print(f'Sua pontuação é: {self._player.score}')

    def show_quantity_cards(self):
        print(f"Ainda restam {len(self._dealer.get_deck())} cartas no baralho")

    def quantity_cards(self):
        return len(self._dealer.get_deck())

    def show_cards_in_hand_player(self):
        list_card_names = []
        for card in self._player.get_hand():
            list_card_names.append(card.get_name())
        list_card_names = str(list_card_names).replace("'", '')
        list_card_names = list_card_names.replace('[', '')
        list_card_names = list_card_names.replace(']', '')
        print(f"Suas cartas são: {list_card_names}")
