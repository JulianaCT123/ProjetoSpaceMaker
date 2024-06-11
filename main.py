import pygame

pygame.init()
tamanho = (1000,563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Maker")
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
fundo = pygame.image.load("assets/bg.jpg")

branco = (255,255,255)


def jogar():
    posicoes = []
    while True:
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    ponto = (evento.pos)
                    posicoes.append(ponto)
                    #print(ponto)

        tela.fill(branco)
        tela.blit(fundo,(0,0))
        
        for pos in posicoes:
            pygame.draw.circle(tela, branco, ponto, 6)
        
        pygame.display.update()
        clock.tick(60)
jogar()