import pygame, random, math

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
shadow = (192, 192, 192)
orange = (255, 100, 10)
grey = (127, 127, 127)
navy__blue = (0, 0, 100)
powder_blue = (176, 224, 230, 255)
yellow = (255, 255, 0)
purple = (153, 0, 153)


def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def main():
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('pain(t)')
    icon = pygame.image.load('icon.jpg')
    pygame.display.set_icon(icon)

    pygame.draw.rect(screen, shadow, (900, 0, 900, 700))
    pygame.draw.line(screen, grey, (904, 0), (904, 700), 3)
    pygame.draw.line(screen, grey, (1, 0), (1, 700), 3)
    pygame.draw.line(screen, grey, (0, 698), (1000, 698), 3)
    pygame.draw.line(screen, grey, (0, 1), (1000, 1), 3)
    pygame.draw.line(screen, grey, (998, 0), (998, 700), 3)

    font = pygame.font.SysFont("Verdana", 20)
    tools_txt = font.render('Tools:', True, black)

    screen.blit(tools_txt, (910, 119))
    pygame.draw.rect(screen, grey, (910, 145, 80, 120), 2)
    pygame.draw.line(screen, grey, (950, 145), (950, 225), 2)
    pygame.draw.line(screen, grey, (910, 185), (990, 185), 2)
    pygame.draw.line(screen, grey, (910, 225), (990, 225), 2)
    pygame.draw.line(screen, grey, (0, 697), (900, 697), 2)

    brush_png = pygame.transform.scale(pygame.image.load("brush.jpg"), (20, 20))
    eraser_png = pygame.transform.scale(pygame.image.load("eraser.jpg"), (20, 20))
    clear_png = pygame.transform.scale(pygame.image.load("Clear.png"), (30, 30))
    #save_png = pygame.transform.scale(pygame.image.load("save.png"), (98, 50))

    # изоображения прямоугольника и круга на кнопки
    pygame.draw.rect(screen, black, (918, 197, 25, 15), 2)
    pygame.draw.circle(screen, black, (970, 205), 9, 2)
    pygame.draw.polygon(screen, black, [(250, 100), (100, 400), (400, 400)])
    # изображение картинок инструментов кроме фигур на кнопках
    global brush, eraser, clear, save
    #save = screen.blit(save_png, (902, 40))
    screen.blit(clear_png, (936, 230))
    screen.blit(brush_png, (920, 156))
    screen.blit(eraser_png, (960, 158))
    # Секция цветов
    colors_txt = font.render('Colors:', True, black)
    screen.blit(colors_txt, (910, 450))
    # pygame.draw.rect(screen, GREY, (925, 485, 50, 175), 2)
    clr_list = [red, orange, yellow, green, powder_blue, blue, purple, black]
    clr_rect_list = []
    for cl, i in enumerate(range(485, 685, 25), 0):
        pygame.draw.rect(screen, clr_list[cl], (925, i, 50, 25))
        clr_rect_list.append(pygame.Rect((925, i, 50, 25)))

    # создание самих кнопок
    def size_buttons():
        global button
        sz_txt = font.render('Size - ', True, black)
        screen.blit(sz_txt, (909, 298))
        pygame.draw.rect(screen, grey, (910, 335, 80, 80), 2)
        screen.fill(white, (912, 337, 77, 77))
        sz_btn = pygame.transform.scale(pygame.image.load("size.jpg"), (25, 25))
        button = screen.blit(sz_btn, (970, 300))
        pygame.display.flip()

    rect_button = pygame.Rect(912, 187, 38, 38)
    circle_button = pygame.Rect(952, 187, 38, 38)
    triangle_button = pygame.Rect(992, 187, 38, 38)
    brush = pygame.Rect((912, 147, 38, 38))
    eraser = pygame.Rect((952, 147, 38, 38))
    clear = pygame.Rect((912, 227, 78, 38))

    draw_surf = pygame.Surface((900, 694))
    draw_surf.fill(white)
    screen.blit(draw_surf, (3, 3))

    # параметры кисти
    mode = 'none'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 5
    thickness = 2

    size_buttons()

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if (mode == 'brush' or mode == 'eraser') and radius > 2:
                    radius -= 2
                elif (mode == 'rect' or mode == 'circle' or mode == 'triangle') and thickness > 1:
                    thickness -= 1
                mode_check(mode, color)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if (mode == 'brush' or mode == 'eraser') and radius < 37:
                    radius += 2
                elif (mode == 'rect' or mode == 'circle' or mode == 'triangle') and thickness < 10:
                    thickness += 1
                mode_check(mode, color)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                global button

                if brush.collidepoint(x, y):
                    radius = 10
                    if mode != 'brush':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'brush'

                if eraser.collidepoint(x, y):
                    radius = 10
                    if mode != 'eraser':
                        mode = 'eraser'
                        color = white

                if rect_button.collidepoint(x, y):
                    if mode != 'rect':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'rect'

                if circle_button.collidepoint(x, y):
                    if mode != 'circle':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'circle'

                if triangle_button.collidepoint(x, y):
                    if mode != 'triangle':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'triangle'

                if button.collidepoint(x, y):
                    if y > 312:
                        if (mode == 'brush' or mode == 'eraser') and radius > 2:
                            radius -= 2
                        elif (mode == 'rect' or mode == 'circle' or mode == 'triangle') and thickness > 1:
                            thickness -= 1

                    if y < 312:
                        if (mode == 'brush' or mode == 'eraser') and radius < 37:
                            radius += 2
                        elif (mode == 'rect' or mode == 'circle' or mode == 'triangle') and thickness < 10:
                            thickness += 1

                if clear.collidepoint(x, y):
                    draw_surf.fill(white)
                    screen.blit(draw_surf, (3, 3))

                if mode == 'brush' or mode == 'rect' or mode == 'circle' or mode == 'triangle':
                    for i, col in enumerate(clr_rect_list, 0):
                        if col.collidepoint(x, y):
                            color = clr_list[i]

                def mode_check(mode, color):
                    if mode == 'none':
                        color = white

                    if mode == 'brush':
                        screen.fill(white, (912, 337, 77, 77))
                        pygame.draw.circle(screen, color, (950, 375), radius)
                    elif mode == 'rect':
                        screen.fill(white, (912, 337, 77, 77))
                        pygame.draw.rect(screen, color, (930, 355, 40, 40), thickness)
                    elif mode == 'circle':
                        screen.fill(white, (912, 337, 77, 77))
                        pygame.draw.circle(screen, color, (950, 375), 30, thickness)
                    elif mode == 'triangle':
                        screen.fill(white, (912, 337, 77, 77))
                        pygame.draw.polygon(screen, color, [(950, 375), (375, 400), (400, 400)], thickness)
                    elif mode == 'eraser':
                        screen.fill(white, (912, 337, 77, 77))
                        pygame.draw.circle(screen, grey, (950, 375), radius, 2)

                if mode == 'brush' or mode == 'eraser':
                    pygame.draw.circle(draw_surf, color, (event.pos[0], event.pos[1]), radius)
                    screen.blit(draw_surf, (3, 3))

                draw_on = True
                mode_check(mode, color)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                draw_on = False
                x2, y2 = event.pos
                if x > x2:
                    x, x2 = x2, x
                if y > y2:
                    y, y2 = y2, y

                if mode == 'rect':
                    pygame.draw.rect(draw_surf, color, (x - 3, y - 3, abs(x2 - (x - 3) - 3), abs(y2 - (y - 3) - 3)),
                                     thickness)
                    screen.blit(draw_surf, (3, 3))

                elif mode == 'circle':
                    pygame.draw.ellipse(draw_surf, color, (x - 3, y - 3, abs(x2 - (x - 3) - 3), abs(y2 - (y - 3) - 3)),
                                        thickness)
                    screen.blit(draw_surf, (3, 3))

                elif mode == 'triangle':
                    pygame.draw.ellipse(draw_surf, color, (x - 3, y - 3, abs(x2 - (x - 3) - 3), abs(y2 - (y - 3) - 3)),
                                        thickness)
                    screen.blit(draw_surf, (3, 3))

            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    if mode == 'brush' or mode == 'eraser':
                        draw_line(draw_surf, last_pos, event.pos, radius, color)
                        screen.blit(draw_surf, (3, 3))

                last_pos = event.pos
        if mode == 'brush' or mode == 'eraser':
            x, y = pygame.mouse.get_pos()
            if x < 900 - radius and x > radius + 3:
                if y > radius and y < 695 - radius:
                    pygame.mouse.set_visible(False)
                    screen.blit(draw_surf, (3, 3))
                    if x + (radius * 2) < 900 - radius and x - (radius * 2) > radius + 3:
                        if y + (radius * 2) < 695 - radius and y - (radius * 2) > radius:
                            if mode == 'brush':
                                pygame.draw.circle(screen, color, (x + 3, y + 3), radius)
                            else:
                                pygame.draw.circle(screen, grey, (x + 3, y + 3), radius, 3)
            elif x > 900 - radius:
                pygame.mouse.set_visible(True)

        pygame.display.flip()

    pygame.quit()


main()