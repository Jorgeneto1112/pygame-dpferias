import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('cachorro tela inical.jpg')

game = True

font = pygame.font.SysFont(None, 90)
text = font.render('cachorros loucos', True, (255, 0, 0))
font2 = pygame.font.SysFont(None, 58)
text2 = font2.render('Pressione qualquer tecla', True, (255, 255, 255))
text3 = font2.render('para jogar novamente', True, (255, 255, 255))
image = pygame.image.load('imagens/cachorroi.png').convert()
image_menor = pygame.transform.scale(image, (800, 600))



while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0, 0, 0)) 
    window.blit(image_menor, (0, 0))
    window.blit(text, (140, 10))
    window.blit(text2, (140, 520))
    window.blit(text3, (170, 550))
    pygame.display.update()  

pygame.quit() 