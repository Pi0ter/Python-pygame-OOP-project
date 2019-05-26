import os
import pygame

pygame.font.init()
font = pygame.font.Font(None, 60)
text_winnig = font.render("Gratulacje! Wygrałeś", True, (0, 254, 0))
text_losing = font.render("Przegrałeś!", True, (254, 0, 0))

buttL = pygame.image.load('game1/button_L.png')
buttLa = pygame.image.load('game1/button_L_light.png')
buttR = pygame.image.load('game1/button_R.png')
buttRa = pygame.image.load('game1/button_R_light.png')
buttS = pygame.image.load('game1/button_O.png')
buttSa = pygame.image.load('game1/button_O_light.png')


background = pygame.image.load('game1/chest.png')

sprites_of_letters = [pygame.image.load(os.path.join('game1/letter_A.png')),
                      pygame.image.load(os.path.join('game1/letter_B.png')),
                      pygame.image.load(os.path.join('game1/letter_C.png')),
                      pygame.image.load(os.path.join('game1/letter_D.png')),
                      pygame.image.load(os.path.join('game1/letter_E.png')),
                      pygame.image.load(os.path.join('game1/letter_F.png')),
                      pygame.image.load(os.path.join('game1/letter_G.png')),
                      pygame.image.load(os.path.join('game1/letter_H.png')),
                      pygame.image.load(os.path.join('game1/letter_J.png')),
                      pygame.image.load(os.path.join('game1/letter_K.png')),
                      pygame.image.load(os.path.join('game1/letter_N.png')),
                      pygame.image.load(os.path.join('game1/letter_O.png')),
                      pygame.image.load(os.path.join('game1/letter_P.png')),
                      pygame.image.load(os.path.join('game1/letter_R.png')),
                      pygame.image.load(os.path.join('game1/letter_S.png')),
                      pygame.image.load(os.path.join('game1/letter_X.png')),
                      pygame.image.load(os.path.join('game1/letter_Z.png'))
                      ]


sprite_of_frame = pygame.image.load(os.path.join('game1/frame.png'))
# rescaling

sprite_of_frame = pygame.transform.scale(sprite_of_frame, (180, 122))

for _ in range(len(sprites_of_letters)):
    sprites_of_letters[_] = pygame.transform.scale(sprites_of_letters[_], (90, 120))
