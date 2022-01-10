#-*-coding:utf8;-*-
#qpy:console

import pygame
pygame.init()
pygame.mixer.music.load('b.mp3')
pygame.mixer.music.play()
pygame.event.wait()