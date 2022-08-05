# pygame-dpferias

# Autor:
Jorge Gyotoku Neto

# Nome do jogo:
Cachorros loucos

# Descrição do jogo:
Busquei desenvolver um jogo relacionado com algo que eu tenha interesse, nisso resolvi desenvolver um jogo sobre cachorros. Com isso surgiu a idéia do jogo chamado cachorros loucos., no qual envolve imagens de diferentes cachorros engraçados e loucos.

# Jogabilidade:
O jogo irá envolver um carro que o jogador irá controlar para desviar dos diferentes cachorros que iram surgindo de cima e embaixo , sua pontuação dependerá de quanto tempo o indivíduo sobreviver e um som de um cachorro gritando tocará ao colidir com o carro, quando os coracoes acabarem você perdeu o jogo e a tela final aparecera.

# Como executar o jogo:

# Link do vídeo do gameplay do jogo:
        pygame.mixer.music.load('audio/dudu.mp3')
        pygame.mixer.music.set_volume(0.4)
        assets['grito'] = pygame.mixer.Sound('audio/grito.mp3')


        pygame.mixer.music.load('audio/dudu.mp3')
        pygame.mixer.music.set_volume(0.4)    
        pygame.display.update() 
        pygame.mixer.music.play(loops=-1)