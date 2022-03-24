import pygame
import button

#init pygame with all modules
pygame.init()


class Buetton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #mouse position
        mouse_pos = pygame.mouse.get_pos()

        #mouseover and conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #button on surface
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


def Mainmenu(callback, screen):  # Mainmenu
    HEIGHT = 1280
    WIDTH = 720
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    #load images
    bg_1_img = pygame.image.load('./Menü/Images/Bg_1.png')
    bg_2_img = pygame.image.load('./Menü/Images/Bg_2.png')
    bg_3_img = pygame.image.load('./Menü/Images/Bg_3.png')
    bg_4_img = pygame.image.load('./Menü/Images/Bg_4.png')
    bg_5_img = pygame.image.load('./Menü/Images/Bg_5.png')
    bg_1_button_img = pygame.image.load('./Menü/Images/Bg_button_1.png')
    bg_2_button_img = pygame.image.load('./Menü/Images/Bg_button_2.png')
    bg_3_button_img = pygame.image.load('./Menü/Images/Bg_button_3.png')
    bg_4_button_img = pygame.image.load('./Menü/Images/Bg_button_4.png')
    bg_5_button_img = pygame.image.load('./Menü/Images/Bg_button_5.png')
    start_img = pygame.image.load('./Menü/Images/Start_img.png')
    nein_img = pygame.image.load('./Menü/Images/ja2.png')
    ja_img = pygame.image.load('./Menü/Images/ja.png')
    anleitung_img = pygame.image.load(
        './Menü/Images/Anleitung_img.png').convert_alpha()

    mod_1_img = pygame.image.load('./Menü/Images/Mod_1.png')
    mod_2_img = pygame.image.load('./Menü/Images/Mod_2.png')

    #Create  Buettons
    #@param x , y , image , scale
    start_button = Buetton(450, 50, start_img, 1)
    bg_1_button = Buetton(50, 225, bg_1_button_img, 1)
    bg_2_button = Buetton(125, 225, bg_2_button_img, 1)
    bg_3_button = Buetton(200, 225, bg_3_button_img, 1)
    bg_4_button = Buetton(275, 225, bg_4_button_img, 1)
    bg_5_button = Buetton(350, 225, bg_5_button_img, 1)
    anleitung_button = Buetton(50, 300, anleitung_img, 1)
    partner_button = Buetton(500, 300, ja_img, 1)
    Mod1_button = Buetton(100, 100, mod_1_img, 1)
    Mod2_button = Buetton(250, 100, mod_2_img, 0.9)

    #Text
    font = pygame.font.Font(None, 32)
    text1 = 'Willst du mit einem Partner spielen?'
    text = font.render(text1, True, (0, 0, 0), None)
    text_rect = text.get_rect()
    text_rect.topleft = (600, 600)

    input_rect = pygame.Rect(100, 100, 150, 28)

    #Mainloop
    #var
    background = bg_1_img
    partner = False
    #modus für Kartenstil True = 1 und False = 2
    Mode = True
    #Playername
    name = 'Player Name'
    gameActive = True

    while gameActive:

        #background
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        #playername
        name_surface = font.render(name, True, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        screen.blit(name_surface, (input_rect.x + 5, input_rect.y + 3))

        #buttons
        if start_button.draw(screen):
            #hier Start def einfügen
            callback()

        if bg_1_button.draw(screen):
            background = bg_1_img
        if bg_2_button.draw(screen):
            background = bg_2_img
        if bg_3_button.draw(screen):
            background = bg_3_img
        if bg_4_button.draw(screen):
            background = bg_4_img
        if bg_5_button.draw(screen):
            background = bg_5_img

        if anleitung_button.draw(screen):
            Anleitung(background, screen)

        if partner_button.draw(screen):
            if partner:
                partner_button.image = ja_img
                partner = False
            else:
                partner_button.image = nein_img
                partner = True

        if Mod1_button.draw(screen):
            Mode = True
        if Mod2_button.draw(screen):
            Mode = False

        #Partner spielen
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) > 10:
                    break
                else:
                    name += event.unicode

        pygame.display.update()


def Anleitung(background, screen):  # anleitung

    running = True
    anleitung_text_img = pygame.image.load(
        'Images\Anleitung_text.png').convert_alpha()
    anleitung_text_button = Buetton(25, 25, anleitung_text_img, 1)
    while running:

        screen.blit(background, (0, 0))

        #place anleitung
        if anleitung_text_button.draw(screen):
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
