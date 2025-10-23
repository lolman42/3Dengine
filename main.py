import pygame
from readobj import readobj, readfaces, readvertex

pygame.init()

fov = 500
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D GAME')

class object3d:
    def __init__(self, vertices, faces, speed):
        self.vertices = vertices
        self.faces = faces
        self.speed = speed

    def projection(self, vertex):
        z = fov + vertex[2]
        if z < 0.1:
            z = 0.1
        projectedX = vertex[0] * fov / z
        projectedY = vertex[1] * fov / z
        screenX = int(projectedX + WIDTH / 2)
        screenY = int(-projectedY + HEIGHT / 2)
        return screenX, screenY
    
    def move(self, x, y, z):
        for vertex in self.vertices:
            vertex[0] += x
            vertex[1] += y
            vertex[2] += z

    def draw(self, screen):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.move(-self.speed, 0, 0)
        if keystate[pygame.K_d]:
            self.move(self.speed, 0, 0)
        if keystate[pygame.K_w]:
            self.move(0, self.speed, 0)
        if keystate[pygame.K_s]:
            self.move(0, -self.speed, 0)
        if keystate[pygame.K_q]:
            self.move(0, 0, -self.speed)
        if keystate[pygame.K_e]:
            self.move(0, 0, self.speed)
        for face in self.faces:
            for i in range(len(face)):
                try:
                    # obj indices start at 1, so subtract 1
                    v1 = self.vertices[int(face[i]) - 1]
                    v2 = self.vertices[int(face[(i + 1) % len(face)]) - 1]
                    start = self.projection(v1)
                    end = self.projection(v2)
                    pygame.draw.line(screen, (255, 255, 255), start, end, 1)
                except:
                    continue

football_v, football_f = readobj("football.obj")
football_v = readvertex(football_v)
football_f = readfaces(football_f)
football = object3d(football_v, football_f, 1)
football.move(0,0,2500)

monkey_v, monkey_f = readobj("monkey.obj")
monkey_v = readvertex(monkey_v)
monkey_f = readfaces(monkey_f)
monkey = object3d(monkey_v, monkey_f, 0.01)
monkey.move(0,0,-500)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    monkey.draw(screen)
    pygame.display.flip()
pygame.quit()
