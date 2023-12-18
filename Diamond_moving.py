import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

vertices = (
    (1, 0, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
    (0, 5),
    (1, 5),
    (2, 5),
    (3, 5)
)

surfaces = (
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4),
    (0, 1, 5),
    (1, 2, 5),
    (2, 3, 5),
    (3, 0, 5)
)

colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Cyan
]

def draw_diamond():
    glBegin(GL_TRIANGLES)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i % len(colors)])  # Apply colors in a repeating pattern
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glEnable(GL_DEPTH_TEST)

    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0, 0.1)  # Move forward
        if keys[pygame.K_s]:
            glTranslatef(0, 0, -0.1)  # Move backward
        if keys[pygame.K_a]:
            glTranslatef(-0.1, 0, 0)  # Move left
        if keys[pygame.K_d]:
            glTranslatef(0.1, 0, 0)  # Move right

        # Rotate the diamond continuously
        glRotatef(1, 0, 1, 0)
        rotation_angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_diamond()

        pygame.display.flip()
        pygame.time.wait(15)

if __name__ == '__main__':
    main()
