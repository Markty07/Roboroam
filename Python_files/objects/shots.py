from random import randint

class Shot :
    def __init__(self, texture, launchposition=[0,0,0], offset_positions = None, damage=1, hp=-1, speed=20) : # speed en pixels/frame
        self.texture = texture
        self.damage = damage
        self.hp = hp # -1 is invulnerable
        self.speed = speed
        self.position = launchposition
        
        if offset_positions != None : # Sert pour des multicannons.
            r = randint(len(offset_positions))
            for i in range(3) :
                self.position[i] += offset_positions[r][i]

    def get_pos(self) :
        return self.position

    def update_pos(self) :
        pass

    def check_collision(self, object_pos_list) :
        pass