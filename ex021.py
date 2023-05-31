""""
Esse algoritmo deve ser capaz de escolher e reproduzir um som em .mp3.
"""

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
