from math import sqrt, cos, sin, radians

class Vector :
    def __init__(self, x, y) :
        self.vecX = x
        self.vecY = y

    def get_x(self) :
        return self.vecX
    
    def get_y(self) :
        return self.vecY
    
    def get_norm(self) :
        return sqrt(self.vecX**2+self.vecY**2)
    
    def sum_with(self, vector2) :
        # additionne deux vecteurs et retoure un nouveau vecteur. NE REMPLACE PAS L'OBJET SUR LEQUEL CETTE FONCTION EST UTILISEE
        newX = self.vecX + vector2.get_x()
        newY = self.vecY + vector2.get_y()
        return Vector(newX, newY)
    
    def multiply_with(self, vector2) :
        # Does not update the object this method is used with, it returns a new one.
        newX = self.vecX * vector2.get_x()
        newY = self.vecY * vector2.get_y()
        return Vector(newX, newY)   
    
    def multiply_with_factor(self, factor) :
        # Does not update the object this method is used with, it returns a new one.
        newX = self.vecX * factor
        newY = self.vecY * factor
        return Vector(newX, newY)
    
    def scale_to(self, desired_norm) :
        # Returns a new vector, doesn't actually replace the object, because I don't want accidental replacements.
        if self.get_norm() == 0 :
            return self
        return self.multiply_with_factor(desired_norm/self.get_norm())
    
    def relative_rotate(self, refAngle, dAngle) :
        # Returns a new vector, that has the norm of the object and the angle that is the sum of refAngle and dAngle
        oV = create_orientation_vector(refAngle + dAngle)
        return oV.scale_to(self.get_norm)

    def __str__(self) : #j'ai oublié comment faire ça x'3
        return(str(self.vecX) + "," + str(self.vecY))

def create_orientation_vector(angle) :
    angle = radians(angle)
    oVector = Vector(-cos(angle), -sin(angle))
    return oVector


# Tests


vecteurA = Vector(2, 3)
vecteurB = Vector(5, 4)

'''
vecteurC = vecteurA.sum_with(vecteurB)
print(vecteurC)
vecteurD = vecteurA.multiply_with(vecteurB)
print(vecteurD)
vecteurE = vecteurA.multiply_with_factor(2)
print(vecteurE)
'''

print(vecteurA.scale_to(50))