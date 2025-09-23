from math import sqrt, cos, sin, radians, acos, asin, atan2

class Vector :
    def __init__(self, x, y) :
        self.vecX = x
        self.vecY = y

    def get_x(self) :
        return self.vecX
    
    def get_y(self) :
        return self.vecY
    
    def get_norm(self) : # Calculates and returns the norm of the vector
        return sqrt(self.vecX**2+self.vecY**2)
    
    def get_angle(self) : # Calculates the absolute angle of the vector
        # oV = scale_vector_to(self, 1)
        return atan2(self.get_y, self.get_x)
    
    def set_vector(self, x, y) : # Sets the coordinates of the vector to x,y. Returns a new vector too JUUUUUST IN CASE.
        self.vecX, self.vecY = x, y
        return Vector(x, y)

    def __str__(self) : #j'ai oublié comment faire ça x'3
        return(str(self.vecX) + "," + str(self.vecY))

def create_orientation_vector(angle) : # Creates a vector thanks to an angle that should be of norm 1
    angle = radians(angle)
    oVector = Vector(cos(angle), -sin(angle))
    return oVector

def sum_vectors(vec1, vec2) : # Adds two vectors together
    newX = vec1.vecX + vec2.vecX
    newY = vec1.vecY + vec2.vecY
    return Vector(newX, newY)

def multiply_vectors(vec1, vec2) : # Multiplies two vectors together
    newX = vec1.vecX * vec2.get_x()
    newY = vec1.vecY * vec2.get_y()
    return Vector(newX, newY)

def multiply_vector_with_factor(vec1, f) : # Multiples a vector by a number
    newX = vec1.vecX * f
    newY = vec1.vecY * f
    return Vector(newX, newY)

def scale_vector_to(vec1, n) :
    if vec1.get_norm() == 0 :
        return vec1
    return multiply_vector_with_factor(vec1, n/vec1.get_norm())

# Tests