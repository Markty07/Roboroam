from random import randint
import math

class ShotBP :
    def __init__(self, texture, damage, speed) :
        self.texture = texture
        self.damage = damage
        self.speed = speed

    def get_texture(self) :
        return self.texture
    def get_damage(self) :
        return self.damage
    def get_speed(self) :
        return self.speed
    
class Shot :
    def __init__(self, shotbp, position) : # Position may be a list of lists, will choose a random one
        pass