from random import randint
import math

class Shot :
    def __init__(self, texture, launchermodel=None, launchposition=[0,0,0], damage=1, hp=-1, speed=20) : # speed en pixels/frame
        self.texture = texture
        self.damage = damage
        self.hp = hp # -1 is invulnerable
        self.speed = speed
        self.position = launchposition
        self.launchermodel = launchermodel

        if launchermodel != False :
            sso = launchermodel.get_shot_spawn_offsets()
            if sso != False :
                if len(sso) == 1 :
                    self.position[0], self.position[1] += sso[0][0], sso[0][1]
                else :
                    r = randint(len(sso)-1)
                    self.position[0], self.position[1] += sso[r][0], sso[r][1]
        

    def get_pos(self) :
        return self.position
    
    def get_damage(self) :
        return self.damage

    def update_pos(self) :
        yvar, xvar = (round(self.speed * math.sin(math.radians(self.position[3]))) * -1), (round(self.speed * math.cos(math.radians(self.position[3]))) * -1)
        self.position[0] += xvar
        self.position[1] += yvar

    def check_collision(self, object_pos_list) : # Needs a list of every damagable object
        pass