

#c =2.pi.r

class circleClass:

    def __init__(self, radius):
        self.radius = radius

    def Circunference(self):
        c = 2 * 3.1416 * self.radius
        print(f"The circunference is : {c} "  )

cir1 = circleClass(5)

cir1.Circunference()
