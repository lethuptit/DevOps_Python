class Bicycle:
    def __init__(self, n, c,p ):
        self._name=n
        self._color=c
        self._speed=p

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def accelerate(self, value):
        self.speed += value

    def __str__(self):
        return f'({self.name} {self.spee}(km/h))'

    def __repr__(self):
        return f'({self.name} {self.speed}(km/h))'

list_bike =[]
for i in range(0,6):
    b = Bicycle(f'Bike_{i}','Black', 5+i)
    list_bike.append(b)

print("List before accelerating:\n", list_bike)
for bike in list_bike:
    if(list_bike.index(bike)%2!=0):
        bike.accelerate(5)

print("List after accelerating:\n", list_bike)