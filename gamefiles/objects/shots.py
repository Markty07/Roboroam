from random import randint
import math

class ShotBP : # Tells to the game which bullet to spawn
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
    
    def set_texture(self, n) :
        self.texture = n
    def set_damage(self, n) :
        self.damage = n
    def set_speed(self, n) :
        self.speed = n
    
class Shot : # Is a spawned bullet
    def __init__(self, shotbp, position) : # Position may be a list of lists, will choose a random one. Determined from model class
        self.texture = shotbp.get_texture()
        self.speed = shotbp.get_speed()
        self.damage = shotbp.get_damage()
        if position[0] is int :
            self.pos = position
        else :
            self.pos = position[randint(len(position))]

    def get_texture(self) :
        return self.texture
    def get_damage(self) :
        return self.damage
    def get_speed(self) :
        return self.speed
    
    def set_texture(self, n) :
        self.texture = n
    def set_damage(self, n) :
        self.damage = n
    def set_speed(self, n) :
        self.speed = n