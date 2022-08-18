
class Location:

    def __init__(self,name,country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and i live in " + self.country + ".")

loc = Location("Ramon", "Mexico")

print(loc.name)
print(loc.country)

print(type(loc))


loc1 = Location("Tomas","Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare","Kenya")
loc4 = Location("Ramon", "Mexico")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
loc4.myLocation()
