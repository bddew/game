import pygame

#Iniciando o PyGame e Criando uma janela
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Jogo MEI T4")


def draw():
    display.fill([19, 173, 235])

gameLoop = True
isPressingW = False
if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Apertou o W!")

        draw()
        pygame.display.update()
