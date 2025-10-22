import pygame
import math

fov = 500

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('3d game')

class object3d:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def projection(self, vertices):
        z = fov + vertices[2]
        if z < 0.1:
            z = 0.1
        projectedX = vertices[0] * fov / z
        projectedY = vertices[1] * fov / z
        return(projectedX,projectedY)
    
    def move(self, x, y, z):
        for vertex in self.vertices:
            vertex[0] += x
            vertex[1] += y
            vertex[2] += z

    def draw(self, screen):
        for face in self.faces:
            for i in range(len(face)):
                start = self.projection(self.vertices[face[i]])
                end = self.projection(self.vertices[face[(i + 1) % len(face)]])
                pygame.draw.line(screen, (255, 255, 255), start, end, 1)

cube = object3d(
    vertices=[
        [-100, -100, -100],
        [ 100, -100, -100],
        [ 100,  100, -100],
        [-100,  100, -100],
        [-100, -100,  100],
        [ 100, -100,  100],
        [ 100,  100,  100],
        [-100,  100,  100]
    ],
    faces=[
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4, 7, 3],
        [0, 4, 5, 1],
        [1, 5, 6, 2],
        [2, 6, 7, 3]
    ]
)

running = True
speed = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        running = False
    if keystate[pygame.K_a]:
        cube.move(-speed, 0, 0)
    if keystate[pygame.K_d]:  
        cube.move(speed, 0, 0)
    if keystate[pygame.K_w]:
        cube.move(0, -speed, 0)
    if keystate[pygame.K_s]:
        cube.move(0, speed, 0)
    if keystate[pygame.K_q]:
        cube.move(0, 0, -speed)
    if keystate[pygame.K_e]:
        cube.move(0, 0, speed)
    
    screen.fill((0,0,0))
    cube.draw(screen)
    pygame.display.flip()