from math import cos, sin, acos, asin

# Every entity has a model that combnes texture, shot spawn offsets, stats. It will replace the player class
# (and player class will be changed to control a model)

class Model : # shot_spawn_offsets are [x,y]
    def __init__(self, texture, shot_spawn_offsets = None) :
        self.texture = texture
        self.shot_spawn_offsets = shot_spawn_offsets

    def get_texture(self) :
        return self.texture
    
    def get_shot_spawn_offsets(self) :
        return self.shot_spawn_offsets
