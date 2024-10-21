import pygame

ANCHO = 800
ALTO = 600

COLOR_FONDO = (0, 0, 0)

class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))

    def jugar(self):
        salir = False
        cont = 0

        while not salir:
            # Bucle principal (main loop)

            cont = cont + 1
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    print("Se ha cerrado la ventana")
                    salir = True

                # print("Se ha producido un evento del tipo:", evento)

            # renderizar mis objetos

            # 1. borrar la pantalla
            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO, ALTO)))
            
            # 2. pintar los objetos en su nueva posición
            rectangulo = pygame.Rect(50, 100, 300, 150)
            pygame.draw.rect(self.pantalla, (cont % 255, 68, 158), rectangulo)

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()




if __name__ == "__main__":
    juego = Pong()
    juego.jugar()







