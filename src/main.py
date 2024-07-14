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
        pygame.display.set_caption("Order 1 Hilbert Curve by David Derflinger")

        self.HC = HilbertCurve()
        self.currentOrder = 1
        self.displayChanged = True

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
                        pygame.display.set_caption("Order " + str(self.currentOrder) + " Hilbert Curve by David Derflinger")
                        self.displayChanged = True
                    if event.key == pygame.K_DOWN:
                        self.currentOrder -= 1
                        if self.currentOrder < 1:
                            self.currentOrder = 1
                        pygame.display.set_caption("Order " + str(self.currentOrder) + " Hilbert Curve by David Derflinger")
                        self.displayChanged = True

            if self.displayChanged:
                currentWidth = self.screen.get_width()
                currentHeight = self.screen.get_height()

                self.screen.fill((50, 50, 50))
                hcArray = self.HC.generate(self.currentOrder)
                print(hcArray)

                oneWidth = currentWidth / len(hcArray)
                oneHeight = currentHeight / len(hcArray[0])

                counter = 1
                lastPoint = [(oneWidth / 2), ((len(hcArray)-1) * oneHeight) + (oneHeight / 2)] # start point
                currentPoint = [len(hcArray)-1, 0]

                while counter < (len(hcArray) * len(hcArray[0])):
                    found = False
                    x = currentPoint[1]
                    y = currentPoint[0]
                    if currentPoint[0]-1 >= 0: # top
                        found = (hcArray[y-1][x] == counter)
                        if found:
                            y = currentPoint[0]-1
                    if currentPoint[1]+1 < len(hcArray[0]) and not found: # right
                        found = (hcArray[y][x+1] == counter)
                        if found:
                            x = currentPoint[1] + 1
                    if currentPoint[0]+1 < len(hcArray) and not found: # bottom
                        found = (hcArray[y+1][x] == counter)
                        if found:
                            y = currentPoint[0] + 1
                    if currentPoint[1]-1 >= 0 and not found: # left
                        found = (hcArray[y][x-1] == counter)
                        if found:
                            x = currentPoint[1] - 1

                    if found:
                        newPoint = [(x * oneWidth) + (oneWidth / 2), (y * oneHeight) + (oneHeight / 2)]
                        pygame.draw.line(self.screen, (0, 100, 150), lastPoint, newPoint, 10)
                        lastPoint = newPoint

                        currentPoint = [y, x]
                    counter += 1

                self.displayChanged = False

            pygame.display.flip()

            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__':
    main = main()
    main.run()
