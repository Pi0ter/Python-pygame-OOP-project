from time import sleep
from load_sprites import *
import settings

import random


class LetterSprites(pygame.sprite.Sprite):
    def __init__(self, window, count_of_sprites, xs, ys, sprites, width_of_letters=90):
        self.fd_up = False
        self.window = window
        self.sprites = sprites
        self.counter = count_of_sprites
        # temporary xs and ys | coords of letter box
        self.xs = xs
        self.ys = ys

        self.w = width_of_letters  # 90
        # Establishing order of sprites with numbers for easier sorting
        self.orderedSprites = []
        self.scrambledSprites = []
        for _ in range(self.counter):
            self.orderedSprites.append(_)
            self.scrambledSprites.append(_)

        # scrambling sprites order

        random.shuffle(self.scrambledSprites)

        print("->" + str(self.scrambledSprites))

        # Making the answer key
        self.solutionOrder = self.solution(self.scrambledSprites)

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, _):
        if _ > 11 or _ < 1:
            raise ValueError("Ilość liter poza określonym zakresem zakresem")
        else:
            self.__counter = _

    @counter.getter
    def counter(self):
        return self.__counter

    @staticmethod
    def solution(xd):
        ready_sol = []
        scrambled = []
        for _ in xd:
            scrambled.append(_)

        for i in range(len(scrambled)):
            for j in range(len(scrambled)-1):
                if scrambled[j] > scrambled[j+1]:
                    ready_sol.append((j, j+1))
                    scrambled[j], scrambled[j+1] = scrambled[j+1], scrambled[j]

        return ready_sol

    def printSolution(self):
        for _ in self.solutionOrder:
            print(_)

    def update(self):
        current_possition = self.xs

        compatibility_table_of_touples = []

        for a in range(len(self.scrambledSprites)):
            compatibility_table_of_touples.append((a, self.sprites[self.scrambledSprites[a]]))

        for i in compatibility_table_of_touples:
            # sprite = i[1]
            self.window.blit(i[1], (current_possition, self.ys))
            # w is size of letters
            current_possition += self.w


class FrameInstance(pygame.sprite.Sprite):
    def __init__(self, window, scrambled, xs, ys, sprite, letter_width):
        self.window = window
        self.xs = xs
        self.ys = ys
        self.frame = sprite
        self.letter_w = letter_width

        # Important Part
        self.letter_obj = scrambled
        self.position = 0
        self.counter_of_moves = 0

    def moveLeft(self):
        if self.position > 0:
            self.position -= 1
            self.update()
            print(self.position, self.position +1)

    def moveRight(self):
        if self.position < len(self.letter_obj.scrambledSprites)-2:
            self.position += 1
            self.update()

    def switch_places(self):

        if self.counter_of_moves >= len(self.letter_obj.solutionOrder):
            return
        else:
            sol = self.letter_obj.solutionOrder[self.counter_of_moves]
            task = (self.position, self.position + 1)
            print(str(sol) + " ->" + str(task))
            if task == sol:
                self.counter_of_moves += 1
                temporary = self.letter_obj.scrambledSprites[self.position]
                self.letter_obj.scrambledSprites[self.position] = self.letter_obj.scrambledSprites[self.position + 1]
                self.letter_obj.scrambledSprites[self.position + 1] = temporary
                self.update()
            else:
                self.letter_obj.fd_up = True
                self.update()

    def update(self):

        if self.letter_obj.fd_up is True:
            self.window.blit(text_losing, (900, 380))

            settings.restart = True

        else:
            px = self.position * self.letter_w + self.xs
            self.letter_obj.update()
            self.window.blit(self.frame, (px, self.ys))

            if self.counter_of_moves >= len(self.letter_obj.solutionOrder):

                self.window.blit(text_winnig, (900, 380))
                settings.restart = True