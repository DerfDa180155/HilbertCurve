import pygame
from HilbertCurve import HilbertCurve


class main:
    def __init__(self):
        # pygame init
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.clock = pygame.time.Clock()

        self.running = True
        self.windowWidth = 1280
        self.windowHeight = 1280

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Hilbert Curve by David Derflinger")

        self.HC = HilbertCurve()
        self.currentOrder = 1

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Quit the Game
                        self.running = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.currentOrder += 1
                    if event.key == pygame.K_DOWN:
                        self.currentOrder -= 1
                        if self.currentOrder < 1:
                            self.currentOrder = 1

            currentWidth = self.screen.get_width()
            currentHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))
            hcArray = self.HC.generate(self.currentOrder)
            print(hcArray)

            oneWidth = currentWidth / len(hcArray)
            oneHeight = currentHeight / len(hcArray[0])

            counter = 0
            lastPoint = []
            while counter < (len(hcArray) * len(hcArray[0])):
                for i in range(len(hcArray)):
                    for j in range(len(hcArray[0])):
                        if hcArray[i][j] == counter:
                            newPoint = [(j * oneWidth) + (oneWidth / 2), (i * oneHeight) + (oneHeight / 2)]
                            if counter != 0:
                                pygame.draw.line(self.screen, (0, 100, 150), lastPoint, newPoint, 1)
                            lastPoint = newPoint
                            counter += 1

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__':
    main = main()
    main.run()
