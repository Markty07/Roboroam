# from model import Model
from ..functions import vectorClass as v

class Player :
    def __init__(self, model, shot, speed=4, hp=20, startlocation = [0, 0, 0]) : # x, y, r (r an angle, uncapped currently)
        self.model = model
        self.shot = shot
        self.pos = startlocation
        self.isfiring = False
        self.hp = hp
        self.speed = speed
        self.mVector = None
        self.active_model_SSO = None

    def move(self, inputs=[0,0,0,0,0,0,0]) : # Z,S,Q,D,A,E,F
        pass

    def update_fire(self, inputs=[0,0,0,0,0,0,0]) :
        self.isfiring = bool(inputs[6])

    def get_firing(self) :
        return self.isfiring
    
    def get_shot(self) :
        return self.shot
    
    def get_model(self) :
        return self.model
    
    def get_pos(self) :
        return self.pos
    
    def get_speed(self) :
        return self.speed
    
    def hp_affect(self, modifier, modifiertype=0) : # Dégâts et soins (0:normal, 1:multiply, 2:set)
        if modifiertype == 0 :
            self.hp += modifier
        elif modifiertype == 1 :
            self.hp = self.hp*modifier
        elif modifiertype == 2 :
            self.hp = modifier

    def get_hp(self) :
        return self.hp
    
    def sGet_mVector(self, vector) :
        if vector == None :
            return self.mVector
        else :
            self.mVector == vector
        
    def update_active_model_SSO(self) :
        pass