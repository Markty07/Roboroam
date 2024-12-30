from math import sqrt, cos, sin, radians, acos, asin, atan2

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
    
    def get_angle(self) :
        oV = self.scaled_to(1)
        return atan2(self.get_y, self.get_x)

    def __str__(self) : #j'ai oublié comment faire ça x'3
        return(str(self.vecX) + "," + str(self.vecY))

def create_orientation_vector(angle) :
    angle = radians(angle)
    oVector = Vector(-cos(angle), -sin(angle))
    return oVector

def sum_vectors(vec1, vec2) :
    # additionne deux vecteurs et retoure un nouveau vecteur.
    newX = vec1.vecX + vec2.get_x()
    newY = vec1.vecY + vec2.get_y()
    return Vector(newX, newY)

def multiply_vectors(vec1, vec2) :
    newX = vec1.vecX * vec2.get_x()
    newY = vec1.vecY * vec2.get_y()
    return Vector(newX, newY)

def multiply_vector_with_factor(vec1, f) :
    newX = vec1.vecX * f
    newY = vec1.vecY * f
    return Vector(newX, newY)

def scale_vector_to(vec1, n) :
    if vec1.get_norm() == 0 :
        return vec1
    return multiply_vector_with_factor(vec1, n/vec1.get_norm())

# Tests