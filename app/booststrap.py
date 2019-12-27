from app.black_jack.black_jack import BlackJack
from app.dealer.dealer import Dealer
from app.jogador.player import Player

player = Player(input("Meu caro, digite seu nome: "))
dealer = Dealer()

black_jack = BlackJack(player, dealer)

black_jack.welcome_mensage()



# black_jack.check_cards()
# black_jack.score_player()
black_jack.check_quantity_cards()
black_jack.dealer_delivering_card()
black_jack.check_quantity_cards()




print('')
print('Obrigado por jogar')