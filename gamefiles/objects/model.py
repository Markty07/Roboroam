from math import cos, sin, acos, asin

# Every entity has a model that combnes texture, shot spawn offsets, stats. It will replace the player class
# (and player class will be changed to control a model)

class Model : # shot_spawn_offsets are [x,y]
    def __init__(self, texture = None) :
        self.texture = texture
        self.shot_spawn_offsets = None # Can be a list of a future bulletspawner object. The model will rotate them.
        self.collider_rule = (0, 0) # index 0 is physics collider, index 1 is bullet collider.
        self.collider_shape = 0 # 0 : Point, 1 : Circle, 2 : rectangle
        self.collider_size = None

    def get_texture(self) :
        return self.texture
    
    def get_shot_spawn_offsets(self) :
        return self.shot_spawn_offsets
