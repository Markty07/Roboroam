class Box :
    def __init__(self, texture, pos=None, hp=20) :
        self.texture = texture
        self.pos = pos
        self.hp = hp

    def hp_affect(self, damage=1, type=0) :
        if self.hp == -1 :
            pass
        elif type == 0 :
            self.hp += damage
            if self.hp < 0 :
                self.hp = 0