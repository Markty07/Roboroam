import pygame
import math
import random

def translate_movement(angle, speed): # Makes stuff move using a vector. Obsolete
    yvar, xvar = (round(speed * math.sin(math.radians(angle))) * -1), (round(speed * math.cos(math.radians(angle))) * -1)
    return [xvar, yvar]

def random_translate(normal_translation, spread) : # Makes bullets move with spread. Obsolete
    return [normal_translation[0] + random.randint(-1*spread, spread), normal_translation[1] + random.randint(-1*spread, spread)]