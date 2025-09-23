from math import cos, sin, radians
from objects import vectorClass as v

class BulletBP :
    def __init__(self, texture, speed, damage, pellets) :
        self.texture = texture
        self.speed = speed
        self.damage = damage
        self.pellets = pellets

defaultbullet = BulletBP("textures/shot_1.png", 10, 1, 1)

class Bulletspawner :
    def __init__(self, initialpos = (0, 0, 0), initialspeed = v.Vector(0, 0), relpos = (0, 0, 0), credit = (0, "default.owner", "default.weapon"), bulletBP = defaultbullet) :
        # What does a bulletspawner need to know :
        # Parent position : Parent will summon the Bulletspawner each frame
        # Angle of the parent object : Parent will transmit
        # Parent velocity vector : Parent will transmit
        # Bullet stats and texture : In object creation
        # Relative position : Needs to know where to be summoned.
        # Relative angle : Last value of relpos in degrees.
        # Bullet team and owner : Do not kill friendlies, credit killer.
        # Bullet count
        self.bpspeed = bulletBP.speed
        self.pos = [0, 0, 0]
        self.pos[2] = (relpos[2] + initialpos[2])%360 # We need bullet properly oriented
        # Let's do math to determine the absolute position of the spawner
        angleRad = radians((initialpos[2]))
        self.pos[0] = -cos(angleRad) + initialpos[0] + (-cos(angleRad)*relpos[0])
        self.pos[1] = sin(angleRad) + initialpos[1] + (sin(angleRad)*relpos[1])
        # adding the bulletBP speed
        self.speed = v.create_orientation_vector(initialpos[2]+relpos[2]+90)
        self.speed = v.multiply_vector_with_factor(self.speed, self.bpspeed)
        self.speed = v.sum_vectors(self.speed, initialspeed)

class Bullet :
    def __init__(self, pos = [0, 0, 0], vector = v.Vector(0, 0), credit = (0, "missing.owner", "missing.weapon"), bulletBP = defaultbullet) :
        # Only needs to move forward every frame
        self.pos = pos # Third value is angle in degrees.
        self.vector = vector
        self.team = credit
        self.texture = bulletBP.texture
        self.damage = bulletBP.damage
        self.lifetime = 30

    def cycle(self, UMV) :
        assert type(UMV) == v.Vector
        self.pos[0] += self.vector.vecX + UMV.vecX
        self.pos[1] += self.vector.vecY + UMV.vecY
        self.lifetime -= 1