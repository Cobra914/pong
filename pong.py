import pygame

pygame.init()
pantalla = pygame.display.set_mode((800,600))

salir = False

while not salir:
    # Bucle principal (main loop)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("Se ha cerrado la ventana")
            salir = True

        print("Se ha producido un evento del tipo:", evento)

    # renderizar mis objetos

    # 1. borrar la pantalla
    pygame.draw.rect(pantalla, (0, 0, 0), ((0,0), (800, 600)))
    
    # 2. pintar los objetos en su nueva posición
    rectangulo = pygame.Rect(50, 100, 300, 150)
    pygame.draw.rect(pantalla, (255, 255, 255), rectangulo)

    # mostrar los cambios en la pantalla
    pygame.display.flip()

pygame.quit()