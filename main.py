import pygame

#Iniciando o PyGame e Criando uma janela
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Jogo MEI T4")

gameLoop = True


# Se "repete" durante o jogo inteiro.
if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            print("Segurando W!")

        # Desenhando as Coisas.
        # Draw :
        display.fill([19, 173, 235])
                            #  x,  y,  width, height
        player  = pygame.Rect( 50, 50, 90, 190,)
        pygame.draw.rect(display, [255, 255, 255, 255], player )

        pygame.display.update()
