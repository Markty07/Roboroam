class BgTiles :
    def __init__(self, size, corner) :
        self.size = size # en pixel
        self.corner = corner # 0-3, top left to bottom right
        self.position = [0, 0] # y/x position

    def update_pos(self, player_position) :
        pass # nom explicatif. Utiliser modulo

    def render(self, player_pos) :
        pass # s'affiche sur l'écran.