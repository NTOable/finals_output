class Vector :
    def __init__(self,x,y) :
        self.x = x
        self.y = y

    def __add__(self,other) :
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __str__(self) :
        return f"New vector: ({self.x},{self.y})"

v1 = Vector(4,6)
v2 = Vector(0,2)
v3 = Vector(12,-11)
v4 = Vector(-3,9)

resultant1 = v1 + v2
resultant2 = v3 + v4

print(resultant1)
print(resultant2)
