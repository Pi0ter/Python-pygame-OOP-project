# from load_sprites import *
from classes import *
import settings
import pygame

pygame.init()

running = True

os.environ['SDL_VIDEO_CENTERED'] = '1'

window_y = 1080
window_x = 1920
window = pygame.display.set_mode((window_x, window_y))

pygame.display.set_caption("Game 1")
bg = background

window.blit(bg, (0, 0))
pygame.display.flip()


# Buttons set up
btnL = buttL.convert_alpha()
btnL = btnL.get_rect()
btnL.center = (590, 400)
btnLa = buttLa.convert_alpha()
btnLa = btnLa.get_rect()
btnLa.center = (590, 400)

btnR = buttR.convert_alpha()
btnR = btnR.get_rect()
btnR.center = (780, 400)
btnRa = buttRa.convert_alpha()
btnRa = btnRa.get_rect()
btnRa.center = (780, 400)

btnS = buttS.convert_alpha()
btnS = btnS.get_rect()
btnS.center = (1450, 400)
btnSa = buttSa.convert_alpha()
btnSa = btnSa.get_rect()
btnSa.center = (1450, 400)

# Position of sprite/letter box
xs = 542
ys = 185
letters_object = None
frame_object = None

# --------------------------------------------- Game Init


def new_game():
    print("-"*30)
    print("-"*10 + "New Game" + "-"*10)
    global letters_object
    global frame_object

    if letters_object:
        del letters_object

    if frame_object:
        del frame_object
    settings.restart = False
    letters_object = LetterSprites(window, 6, xs, ys, sprites_of_letters)

    frame_object = FrameInstance(window, letters_object, xs, ys, sprite_of_frame, letters_object.w)

    letters_object.printSolution()
    settings.get_slept()

# ----------------------------------------- MAIN LOOP


while running:
    if settings.restart is True:
        new_game()

    pygame.time.delay(17)
    window.blit(bg, (0, 0))

    window.blit(buttL, btnL)
    window.blit(buttR, btnR)
    window.blit(buttS, btnS)

    letters_object.update()
    frame_object.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and btnL.collidepoint(pygame.mouse.get_pos()):
            window.blit(buttLa, btnLa)
            frame_object.moveLeft()
        if event.type == pygame.MOUSEBUTTONDOWN and btnR.collidepoint(pygame.mouse.get_pos()):
            window.blit(buttRa, btnRa)
            frame_object.moveRight()
        if event.type == pygame.MOUSEBUTTONDOWN and btnS.collidepoint(pygame.mouse.get_pos()):
            window.blit(buttSa, btnSa)
            frame_object.switch_places()

    pygame.display.flip()

pygame.quit()
exit()










