from app.cards.cards import Card
from app.dealer.dealer import Dealer
from app.player.player import Player


class BlackJack:
    def __init__(self, player: Player, dealer: Dealer):
        self._player = player
        self._dealer = dealer

    def welcome_message(self):
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
        if (card.get_value() == 'Q'
                or card.get_value() == 'J'
                or card.get_value() == 'K'):
            self._player.score += 10
        else:
            self._player.score += card.get_value()

    def show_result_message(self):
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
        return self._dealer.want_continue(self._player)

    @staticmethod
    def show_retired_card(card: Card):
        print(f'A carta retirada foi: {card.get_name()}')

    def show_score_player(self):
        print(f'Sua pontuação é: {self._player.score}')

    def show_quantity_cards(self):
        print(f"Ainda restam {len(self._dealer.get_deck())} cartas no baralho")

    def quantity_cards(self):
        return len(self._dealer.get_deck())

    def check_if_has_result(self):
        if self._player.score == 21 or self._player.score > 21:
            return True

    def show_cards_in_hand_player(self):
        list_card_names = []
        for card in self._player.get_hand():
            list_card_names.append(card.get_name())
        list_card_names = str(list_card_names).replace("'", '')
        list_card_names = list_card_names.replace('[', '')
        list_card_names = list_card_names.replace(']', '')
        print(f"Suas cartas são: {list_card_names}")




    @staticmethod
    def farewell_message(black_jack):
        print(("=" * 60))
        black_jack.show_result_message()
        print(("=" * 60))
        print('Obrigado por utilizar este produto')
        print(("=" * 60), '\n')
        input('Pressione Enter para finalizar')



