
import pygame
import random
#loop para reiniciar
jogao=True
while jogao==True:
    pygame.init()
    pygame.mixer.init()

    #Gera tela principal
    WIDTH = 1000
    HEIGHT = 800
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('cachorro')

    #Inicia assets
    FPS = 30
    cachorro_WIDTH = 60
    cachorro_HEIGHT = 48
    pessoa_WIDTH = 60
    pessoa_HEIGHT = 48

    def load_assets():
        assets = {}
        assets['fundo'] = pygame.image.load('imagens/so_a_rua.png').convert()
        assets['fundo'] = pygame.transform.scale(assets['fundo'], (WIDTH,2000))
        assets['cachorro_img'] = pygame.image.load('imagens/cachorro1.jpg').convert_alpha()
        assets['cachorro_img'] = pygame.transform.scale(assets['cachorro_img'], (cachorro_WIDTH, cachorro_HEIGHT))
        assets['pessoa_img'] = pygame.image.load('imagens/pessoa.png').convert_alpha()
        assets['pessoa_img'] = pygame.transform.scale(assets['pessoa_img'], (pessoa_WIDTH, pessoa_HEIGHT))
        assets["score_font"] = pygame.font.Font('PressStart2P.ttf', 28)
        assets["fonte"] = pygame.font.Font('PressStart2P.ttf', 32)
        pygame.mixer.music.load('audio/fundo.mp3')
        pygame.mixer.music.set_volume(0.4)
        assets['grito'] = pygame.mixer.Sound('audio/cachorro.mp3')
        return assets

    #Cria classes
    class pessoa(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            pygame.sprite.Sprite.__init__(self)

            self.image = assets['pessoa_img']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
            self.groups = groups
            self.assets = assets

        def update(self):

            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

    class cachorro(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            pygame.sprite.Sprite.__init__(self)

            self.image = assets['cachorro_img']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH-cachorro_WIDTH)
            self.rect.y = random.randint(-100, -cachorro_HEIGHT)
            self.speedx = 18
            self.speedy = 18


        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx *=-1
            if self.rect.left < 0:
                self.rect.left = 0
                self.speedx *=-1
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.speedy *=-1
            if self.rect.top < 0:
                self.rect.top = 0
                self.speedy *=-1
            if random.uniform(0.0,1.0) < 0.03:
                self.speedx *=-1
            if random.uniform(0.0,1.0) < 0.03:
                self.speedy *=-1

    def game_screen(window):
        clock = pygame.time.Clock()

        assets = load_assets()

        # Criando grupo 
        all_sprites = pygame.sprite.Group()
        all_cachorro = pygame.sprite.Group()
        groups = {}
        groups['all_sprites'] = all_sprites
        groups['all_cachorro'] = all_cachorro

        # Criando o jogador
        player = pessoa(groups, assets)
        all_sprites.add(player)
        # Criando o cachorro
        objetivo = cachorro(groups, assets)
        all_cachorro.add(objetivo)
        all_sprites.add(objetivo)

        DONE = 0
        PLAYING = 1
        state = PLAYING

        keys_down = {}
        score = 0
        game= True
        #tela inicial
        while game==True:
                
                pygame.mixer.init()

                game = True

                
                text = assets['fonte'].render('Pega Cachorro', True, (255, 0, 0))
                
                text2 = assets['fonte'].render('Pressione qualquer tecla', True, (255, 255, 255))
                text3 = assets['fonte'].render('para iniciar o jogo', True, (255, 255, 255))
                image = pygame.image.load('imagens/cachorroi.png').convert()
                image_menor = pygame.transform.scale(image, (1000, 800))
                

                while game:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            game= False
                            
                    
                    window.fill((0, 0, 0)) 
                    window.blit(image_menor, (0, 0))
                    window.blit(text, (300, 40))
                    window.blit(text2, (90, 720))
                    window.blit(text3, (130, 750))
                    pygame.display.update()  


        #retomada da musica do fundo    
        pygame.mixer.music.load('audio/fundo.mp3')
        pygame.mixer.music.set_volume(0.4)    
        pygame.display.update() 
        pygame.mixer.music.play(loops=-1)


        #Loop principal
        while state != DONE:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                # Só verifica o teclado se está no estado de jogo
                if state == PLAYING:
                    # Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        
                            keys_down[event.key] = True
                            if event.key == pygame.K_LEFT:
                                player.speedx -= 8
                            if event.key == pygame.K_RIGHT:
                                player.speedx += 8
                            if event.key == pygame.K_UP:
                                player.speedy -= 8
                            if event.key == pygame.K_DOWN:
                                player.speedy += 8
                    
                    if event.type == pygame.KEYUP:
                    
                        if event.key in keys_down and keys_down[event.key]:
                            if event.key == pygame.K_LEFT:
                                player.speedx += 8
                            if event.key == pygame.K_RIGHT:
                                player.speedx -= 8
                            if event.key == pygame.K_UP:
                                player.speedy += 8
                            if event.key == pygame.K_DOWN:
                                player.speedy -= 8

            #Atualiza estado do jogo
            all_sprites.update()
            # Verifica se houve colisão entre jogador e cachorro
            if state == PLAYING:
                hits = pygame.sprite.spritecollide(player, all_cachorro, True, pygame.sprite.collide_mask)
                # pontucao vai aumentando
                score += 1
                

                
                #acaba com o jogo
                if len(hits) > 0:
                    assets['grito'].play()
                    state = DONE

            
            window.fill((0, 0, 0))  
            window.blit(assets['fundo'], (0, 0))
            all_sprites.draw(window)

            # mostra a pontucao
            text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  10)
            window.blit(text_surface, text_rect)


            pygame.display.update()  
        #loop da tela final 
        while state==DONE:
            pygame.mixer.init()

            window = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('cachorro')

            game = True
            sua_pont = assets['fonte'].render('sua pontuacao', True, (255, 255, 0))
            pontuaco = assets['fonte'].render("{:08d}".format(score), True, (255, 255, 0))
            text = assets['fonte'].render('MEUS PARABENS', True, (255, 0, 0))
            text2 = assets['fonte'].render(' VOCE PEGOU ESSE DANADO', True, (255, 0, 0))
            text3 = assets['fonte'].render('Pressione a tecla ENTER', True, (255, 255, 255))
            text4 = assets['fonte'].render('para jogar novamente', True, (255, 255, 255))
            image = pygame.image.load('imagens/cachorrofinal.webp').convert()
            image_menor = pygame.transform.scale(image, (1000,800))


            while game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state=PLAYING
                        game=False
                        jogao = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            state=PLAYING
                            game= False
                            jogao = True
                window.fill((0, 0, 0)) 
                window.blit(image_menor, (0, 0))
                window.blit(sua_pont,(300,200))
                window.blit(pontuaco,(370,240))
                window.blit(text, (260, 30))
                window.blit(text2, (120, 70))
                window.blit(text3, (110, 630))
                window.blit(text4, (170, 680))
                pygame.display.update()  
            

    game_screen(window)  

    pygame.quit()

    