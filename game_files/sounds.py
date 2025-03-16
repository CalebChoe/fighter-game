import pygame
pygame.init()

def playsound(name, channel):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(name))

def stopsound(channel):
    pygame.mixer.Channel(channel).stop()

def endlessplay(name, channel):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(name), -1)
