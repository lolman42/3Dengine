import pygame
import math
from readobj import readobj

pygame.init()

fov = 500
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D GAME')

class object3d:
    def __init__(self, vertexes, faces, speed):
        self.vertexes = vertexes
        self.faces = faces
        self.speed = speed

    def projection(self, vertex):
        z = fov + vertex.z
        if z < 0.1:
            z = 0.1
        projectedX = vertex.x * fov / z
        projectedY = vertex.y * fov / z
        screenX = int(projectedX + WIDTH / 2)
        screenY = int(-projectedY + HEIGHT / 2)
        return screenX, screenY
    
    def rotateX(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        for vertex in self.vertexes:
            y = vertex.y * cos - vertex.z * sin
            z = vertex.z * cos + vertex.y * sin
            vertex.y = y
            vertex.z = z

    def rotateY(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        for vertex in self.vertexes:
            x = vertex.x * cos - vertex.z * sin
            z = vertex.z * cos + vertex.x * sin
            vertex.x = x
            vertex.z = z

    def rotateZ(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        for vertex in self.vertexes:
            x = vertex.x * cos - vertex.y * sin
            y = vertex.y * cos + vertex.x * sin
            vertex.x = x
            vertex.y = y
        

    def getModelOrigin(self):       
        x = [x.x for x in self.vertexes]
        y = [y.y for y in self.vertexes]
        z = [z.z for z in self.vertexes]
        ox = sum(x) / len(x)
        oy = sum(y) / len(y)
        oz = sum(z) / len(z)
        return ox, oy, oz

    
    def move(self, x, y, z):
        for vertex in self.vertexes:
            vertex.x += x
            vertex.y += y
            vertex.z += z

    def draw(self, screen, color):
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
        if keystate[pygame.K_RIGHT]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz) # go to 0,0,0
            self.rotateY(-0.01)
            self.move(ox, oy, oz) # go back to where it was
        if keystate[pygame.K_LEFT]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz)
            self.rotateY(0.01)
            self.move(ox, oy, oz)
        if keystate[pygame.K_UP]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz)
            self.rotateX(0.01)
            self.move(ox, oy, oz)
        if keystate[pygame.K_DOWN]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz)
            self.rotateX(-0.01)
            self.move(ox, oy, oz)
        if keystate[pygame.K_SLASH]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz)
            self.rotateZ(-0.01)
            self.move(ox, oy, oz)
        if keystate[pygame.K_RSHIFT]:
            ox, oy, oz = self.getModelOrigin()
            self.move(-ox, -oy, -oz)
            self.rotateZ(0.01)
            self.move(ox, oy, oz)
        for face in self.faces:
            for i in range(len(face)):
                try:
                    # obj indices start at 1, so subtract 1
                    v1 = self.vertexes[int(face[i]) - 1]
                    v2 = self.vertexes[int(face[(i + 1) % len(face)]) - 1]
                    start = self.projection(v1)
                    end = self.projection(v2)
                    pygame.draw.line(screen, color, start, end, 1)
                except:
                    continue

football_v, football_f = readobj("football.obj")
football = object3d(football_v, football_f, 5)
football.move(0,0,2500)

monkey_v, monkey_f = readobj('monkey.obj')
monkey = object3d(monkey_v, monkey_f, 0.01)
monkey.move(0,0,-500)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    football.draw(screen, (0,0,0))
    pygame.display.flip()
pygame.quit()
