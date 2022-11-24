import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.10)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Victory.mp3')
pygame.mixer.music.play(-1)

audio_colisao = pygame.mixer.Sound('smw_coin.wav')
audio_colisao.set_volume(1)

largura = 640
altura = 480
velocidade = 5
morreu = False
pausado = False
x_cobra = int(largura/2)
y_cobra = int(altura/2)
x_controle = velocidade
y_controle = 0
x_maca = randint(20, 620)
y_maca = randint(20, 460)
fonte = pygame.font.SysFont("Baskerville", 30, True, True)
pontos = 0
lista_cobra = []
comprimento_inicial = 5


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

def reiniciar_jogo():
        global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu, velocidade
        pontos = 0
        comprimento_inicial = 5
        x_cobra = int(largura/2)
        y_cobra = int(altura/2)
        lista_cobra = []
        lista_cabeca = []
        x_maca = randint(20, 620)
        x_maca = randint(20, 460)
        morreu = False
        velocidade = 5

def aumenta_cobra(lista_cobra):
        for xey in lista_cobra:
            #xey = [x,y]
            #xey[0] = x
            #xey[1] = y
            pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 25, 25))

def pausar():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    pausado = False
        
        fonte3 = pygame.font.SysFont('arial', 20, False, True)
        mensagem3 = 'PAUSADO aperte c para continuar'
        texto_formatado = fonte3.render(mensagem3, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()

        ret_texto.center = (largura//2, altura//2)
        tela.blit(texto_formatado, ret_texto)

        pygame.display.update()
        relogio.tick(5)


while True:
        relogio.tick(60)
        tela.fill((0, 0, 0))
        mensagem = (f'Pontos: {pontos}')
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

                if event.key == K_p:
                    if pausado == False:
                        pausar()
                    

        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle

        cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 25, 25))
        maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 25, 25))

        

        if cobra.colliderect(maca):
            x_maca = randint(20, 620)
            y_maca = randint(20, 460)
            pontos += 1
            audio_colisao.play()
            comprimento_inicial = comprimento_inicial + 1
            velocidade = velocidade + 0.2
            if velocidade >= 20:
                velocidade == 20

        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)

        lista_cobra.append(lista_cabeca)

        if lista_cobra.count(lista_cabeca) > 1:

            fonte2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game over! Pressione a tecla R para jogar novamente'
            texto_formatado = fonte2.render(mensagem, True, (255, 0, 0))
            ret_texto = texto_formatado.get_rect()

            morreu = True
            while morreu:
                tela.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()

                ret_texto.center = (largura//2, altura//2)
                tela.blit(texto_formatado, ret_texto)

                pygame.display.update()

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        aumenta_cobra(lista_cobra)

        tela.blit(texto_formatado, (40, 20))

        if x_cobra < 0:
            x_cobra = largura
        if x_cobra > largura:
            x_cobra = 0
        if y_cobra < 0:
            y_cobra = altura
        if y_cobra > altura:
            y_cobra = 0

        pygame.display.update()
