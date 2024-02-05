

class model :
    def __init__(self, texture, shot_spawn_offsets = None) :
        self.texture = texture
        self.shot_spawn_offsets = shot_spawn_offsets

    def get_texture(self) :
        return self.texture
    
    def get_shot_spawn_offsets(self) :
        return self.shot_spawn_offsets