import pygame

ALTO = 600
ANCHO = 800
ALTO_PALA = 100
ANCHO_PALA = 20
MARGEN = 30

COLOR_FONDO = (0, 0, 0)
COLOR_OBJETOS = (200, 200, 200)
VEL_JUGADOR = 10
FPS = 40


class Pintable(pygame.Rect):

    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)


class Pelota(Pintable):

    tam_pelota = 10

    def __init__(self):
        # definido, construido, instanciado... el rectangulo
        super().__init__(
            (ANCHO - self.tam_pelota) / 2,
            (ALTO - self.tam_pelota) / 2,
            self.tam_pelota,
            self.tam_pelota)

class Jugador(Pintable):

    def __init__(self, x):
        arriba = (ALTO - ALTO_PALA) / 2
        super().__init__(x, arriba, ANCHO_PALA, ALTO_PALA)
    
    def subir(self):
        posicion_minima = 0
        self.y -= VEL_JUGADOR
        if self.y < posicion_minima:
            self.y = posicion_minima

    def bajar(self):
        posicion_maxima = ALTO - ALTO_PALA
        self.y += VEL_JUGADOR
        if self.y > posicion_maxima:
            self.y = posicion_maxima

class Pong:

    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        self.reloj = pygame.time.Clock()

        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA)

    def jugar(self):
        salir = False

        while not salir:
            # Bucle principal (main loop)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

            # movimiento jugador    
            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_a]:
                self.jugador1.subir()
            if estado_teclas[pygame.K_z]:
                self.jugador1.bajar()
            if estado_teclas[pygame.K_UP]:
                self.jugador2.subir()
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.bajar()

            # renderizar mis objetos

            # 1. borrar la pantalla
            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO, ALTO)))
            
            # 2. pintar jugador 1 (izquierda)
            self.jugador1.pintame(self.pantalla)

            # 3. pintar jugador 2 (derecha)
            self.jugador2.pintame(self.pantalla)

            # 4. pintar la red
            self.pintar_red()

            # 5. pintar la pelota
            self.pelota.pintame(self.pantalla)

            # mostrar los cambios en la pantalla
            pygame.display.flip()
            self.reloj.tick(FPS)

        pygame.quit()

    def pintar_red(self):
        pos_x = ANCHO / 2

        tramo_pintado = 20
        tramo_vacio = 15
        ancho_red = 6

        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(
                self.pantalla,
                COLOR_OBJETOS,
                (pos_x, y),
                (pos_x, y + tramo_pintado),
                width=ancho_red)








