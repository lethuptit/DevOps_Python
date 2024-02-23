class Car:
    def __init__(self):
        self._name=''
        self._color =''
        self._model=''
        self._brand=''
        self._price=0
        self._weight=0
        self._horsePower=0
        self._

    @property
    def name(self):
        return self._name
    
    @name.setter(self, value):
        self._name =value

    @property
    def color(self):
        return self._color
    
    @color.setter(self, c):
        self._color =c

    @property
    def model(self):
        return self._color
    
    @model.setter(self, m):
        self._model =m
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter(self, b):
        self._brand =b
    
    @property
    def price(self):
        return self._price
    
    @price.setter(self,p):
        self._price =p

    @property
    def weight(self):
        return self._weight
    
    @weight.setter(self, value):
        self._weight =value

    @property
    def horsePower(self):
        return self._horsePower
    
    @horsePower.setter(self, value):
        self._horsePower =value
    
    def __str__(self):
        return f"({self.name} {self.model} {self.price})"
    
    def __repr__(self):
        return f"({self.name} {self.model} {self.price})"