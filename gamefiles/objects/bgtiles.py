

class BgTiles :
    def __init__(self, size, corner) :
        self.size = size # en pixel
        self.corner = corner # 0-3, top left to bottom right
        self.pos= [0, 0] # y/x position

    def init_pos(self, player_position) :  # récupère position du joueur, définit position initale sur l'écran. 
        if self.corner in [0, 1] :
            self.pos[0] = 0
        else :
            self.pos[0] = self.size
        if self.corner in [0, 2] :
            self.pos[1] = 0
        else :
            self.pos[1] = self.size

    def update_pos(self, movement) : # demande réflexion
        pass

    def render(self, player_pos) :  # s'affiche sur l'écran.
        pass