import pygame
from tkinter import simpledialog


pygame.init()
tamanho = (1000,563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Maker")
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
fundo = pygame.image.load("assets/bg.jpg")
fonte = pygame.font.SysFont("Arial",15)

branco = (255,255,255)
tela.fill(branco)

def jogar():
    posicoes = []
    nomes = []
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    while True:
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    ponto = (evento.pos)
                    posicoes.append(ponto)
                    nome = simpledialog.askstring("...", "Qual o nome dessa estrela ?")
                    if not nome:
                        nome = (f"Desconhecido ({ponto[0]}, {ponto[1]})")
                    nomes.append(nome)
                    textoNome = fonte.render(nome,True,branco)
                    tela.blit(textoNome,(ponto))

        for pos in posicoes:
            pygame.draw.circle(tela, branco, pos, 5)
        for item in range(len(posicoes)-1):
            pygame.draw.line(tela,branco,posicoes[item],posicoes[item + 1], 3)

        pygame.display.update()
        clock.tick(60)
jogar()