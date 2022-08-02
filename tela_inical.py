import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('cachorro tela inical.jpg')

game = True

font = pygame.font.SysFont(None, 80)
text = font.render('cachorros loucos', True, (255, 0, 0))
font2 = pygame.font.SysFont(None, 48)
text2 = font2.render('Pressione qualquer tecla', True, (255, 255, 255))
text3 = font2.render('para jogar novamente', True, (255, 255, 255))
image = pygame.image.load('imagens/cachorro tela nova.png').convert()
image_menor = pygame.transform.scale(image, (600, 500))



while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0, 0, 0)) 
    window.blit(image_menor, (0, 0))
    window.blit(text, (80, 10))
    window.blit(text2, (90, 420))
    window.blit(text3, (110, 450))
    pygame.display.update()  

pygame.quit() 