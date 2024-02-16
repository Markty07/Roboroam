import pygame

class BgTiles :
    def __init__(self, size, corner) :
        self.size = size # en pixel
        self.corner = corner # 0-3, top left to bottom right
        self.pos= [0, 0] # x/y position

    def init_pos(self, player_position) :  # récupère position du joueur, définit position initale sur l'écran. 
        if self.corner in [0, 1] :
            self.pos[1] = 0
        else :
            self.pos[1] = self.size
        if self.corner in [0, 2] :
            self.pos[0] = 0
        else :
            self.pos[0] = self.size

    def update_pos(self, keys, movement_speed) : # Z, S, Q, D, A, E, fire
        if keys[0] == 1 :
            self.pos[1] += movement_speed
            if self.pos[1] > self.size :
                self.pos[1] -= 2*self.size
        if keys[1] == 1 :
            self.pos[1] -= movement_speed
            if self.pos[1] <= 2*self.size :
                self.pos[1] += 2*self.size
        if keys[2] == 1 :
            self.pos[0] -= movement_speed
            if self.pos[0] <= 2*self.size :
                self.pos[0] += 2*self.size
        if keys[3] == 1 :
            self.pos[0] += movement_speed
            if self.pos[0] > self.size :
                self.pos[0] -= 2*self.size

    def render(self) :  # s'affiche sur l'écran. Probablement inutile
        pass