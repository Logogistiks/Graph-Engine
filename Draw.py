import pygame
from math import sin, cos, atan, sqrt, pi, atan2
from JUtils.JColors import RGB_WHITE, RGB_BLACK, RGB_RED
from random import randint

def sgn(n):
    return n / abs(n)

def deg2rad(deg):
    return deg * pi / 180

def rad2deg(rad):
    return rad * 180 / pi

def pol2cart(ang, r):
    return (r*cos(deg2rad(ang)), r*sin(deg2rad(ang)))

def cart2pol(x, y):
    quad_dict = {(1, 1): 0,
                 (-1, 1): 180,
                 (-1, -1): 180,
                 (1, -1): 360}
    r = sqrt(x*x + y*y)
    th = rad2deg(atan(y/x))+quad_dict[(sgn(x), sgn(y))]
    return (r, th)

def arrow(sc, p1, p2, cl):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    angle = atan2(dy, dx)

    arrowhead_length = 20

    x3 = p2[0] - arrowhead_length * cos(angle + pi / 6) # Calculate the coordinates of the end of the arrowhead
    y3 = p2[1] - arrowhead_length * sin(angle + pi / 6)
    x4 = p2[0] - arrowhead_length * cos(angle - pi / 6)
    y4 = p2[1] - arrowhead_length * sin(angle - pi / 6)

    pygame.draw.line(sc, cl, p1, p2, 5)
    pygame.draw.line(sc, cl, p2, (x3, y3), 5)
    pygame.draw.line(sc, cl, p2, (x4, y4), 5)

def get_closer_points(p1, p2, distance):
    # Calculate the slope of the line
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # Calculate the angle of the line
    angle = atan2(dy, dx)

    # Calculate the new points
    x3 = p1[0] + distance * cos(angle)
    y3 = p1[1] + distance * sin(angle)
    x4 = p2[0] - distance * cos(angle)
    y4 = p2[1] - distance * sin(angle)

    return ((x3, y3), (x4, y4))

def draw(gr): # gr = list of nodes

    pygame.init()

    window_size = (1000, 800)
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption('Graph')

    n = len(gr)
    line_width = 2
    spacing = 280 # Set the radius of the big circle
    Cradius = spacing/n # Set the radius of the circles # 30
    angle = 360 / n # Set the angle between each circle
    color = RGB_WHITE # Set the color of the circles
    bg_color = RGB_BLACK
    width, height = window_size
    center = (width // 2, height // 2) # Set the center of the window

    running = True
    while running:
        screen.fill(bg_color)

        circles = {}

        #draw circles
        for i in range(n):
            angle = i * (360 / n) # Calculate the angle of the current circle
            x, y = pol2cart(angle, spacing) # Calculate the x and y coordinates of the circle
            x += center[0]
            y += center[1]

            pygame.draw.circle(screen, color, (x, y), Cradius, line_width)
            circles[gr[i]] = (x, y)

        #draw values
        font = pygame.font.SysFont(None, int(Cradius*2.5))
        for i in range(n):
            img = font.render(str(gr[i].value), True, RGB_WHITE)
            blitX = circles[gr[i]][0] - img.get_size()[0]//2
            blitY = circles[gr[i]][1] - img.get_size()[1]//2
            screen.blit(img, (blitX, blitY))

        #draw connections
        connections = []
        for node in gr:
            connections += [(node, childNode) for childNode in node.childs]
            connections += [(parentNode, node) for parentNode in node.parents]
        connections = list(set(connections)) # remove duplicates

        for arr in connections:
            if arr[0] != arr[1]:
                new = get_closer_points(circles[arr[0]], circles[arr[1]], Cradius)
                arrow(screen, new[0], new[1], RGB_RED)
            else: # self reference
                pygame.draw.circle(screen, RGB_RED, circles[arr[0]], Cradius-3, line_width+3)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()