

class Player :
    def __init__(self, model, shot, startlocation = [0, 0, 0], hp=20) : # x, y, r
        self.model = model
        self.shot = shot
        self.pos = startlocation
        self.isfiring = False
        self.hp = hp

    def move(self, inputs=[0,0,0,0,0,0]) : # Z,S,Q,D,A,E
        pass

    def update_fire(self, inputs=0) :
        self.isfiring = bool(inputs)

    def get_fire(self) :
        return self.isfiring
    
    def hp_affect(self, modifier, modifiertype=0) : # Dégâts et soins (0:normal, 1:multiply, 2:set)
        if modifiertype == 0 :
            self.hp += modifier
        elif modifiertype == 1 :
            self.hp = self.hp*modifier
        elif modifiertype == 2 :
            self.hp = modifier

    def get_hp(self) :
        return self.hp