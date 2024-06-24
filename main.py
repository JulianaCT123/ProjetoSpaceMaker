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


def jogar():
    
    estrelas = {}

    while True:
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    arquivo = open("save.txt","w")
                    arquivo.write(str(estrelas))
                    arquivo.close()
                    quit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    arquivo = open("save.txt","w")
                    arquivo.write(str(estrelas))
                    arquivo.close()
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    nome = simpledialog.askstring("...", "Qual o nome dessa estrela ?")
                    if not nome:
                        nome = (f"Desconhecido {evento.pos}")
                    estrelas[nome] = evento.pos
                    #print(estrelas)
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F1: # F1 para salvar
                    try:
                        arquivo = open("save.txt","w")
                        arquivo.write(str(estrelas))
                        arquivo.close()
                    except:
                        pass
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F2: # F2 para carregar
                    try:
                        tela.fill(branco)
                        arquivo = open("save.txt", "r")
                        estrelas = eval(arquivo.read())
                        arquivo.close()
                    except:
                         pass
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F3: # F3 para excluir todas as marcaçõens
                    estrelas = {}
                    arquivo = open("save.txt","w")
                    arquivo.write(str(estrelas))
                    arquivo.close()
        
        tela.blit(fundo,(0,0))
        
        textoSalvar = fonte.render("Aperte F1 para Salvar os pontos", True, branco)
        tela.blit(textoSalvar, (5,0))
        textoCarregar = fonte.render("Aperte F2 para Carregar os pontos", True, branco)
        tela.blit(textoCarregar,(5,15))
        textoExcluir = fonte.render("Aperte F3 para Excluir todos os pontos", True, branco)
        tela.blit(textoExcluir,(5,30))

        for key, value in estrelas.items():
                textoNome = fonte.render(key,True,branco)
                tela.blit(textoNome,value)
                pygame.draw.circle(tela, branco, value, 5)
        teste = list(estrelas.values())
        for pos in range(len(teste) -1):
                pygame.draw.line(tela,branco, teste[pos], teste[pos +1], 1)

        pygame.display.update()
        clock.tick(60)
jogar()