import random

class Game:
    def __init__(self):
        self.currentNumber = random.randint(1, 9)
        self.tries = 0

    def reset(self):
        self.currentNumber = random.randint(1, 9)
        self.tries = 0

    
    def guess(self, guess):
        self.tries += 1
        if guess > self.currentNumber:
            print('Too high!')
        elif guess < self.currentNumber:
            print('Too low!')
        else:
            print(f'Congratulations! That took {self.tries} tries.')
            self.reset()

class Game_2:
    def __init__(self):
        self.reset()

    def reset(self,minrange=1, maxrange=100 ):
        self.maxValue =maxrange
        self.minValue =minrange
        self.tries = 0

    def setTargetNumber(self, num):
        self.target = num

    def guess(self, low, high):        
        self.tries += 1
        self.maxValue =high
        self.minValue =low
        self.currentNumber = random.randint(self.minValue, self.maxValue)     
        print(f'I will try in [{low},{high}]. I guess... {self.currentNumber}.')   
        return self.currentNumber

    def getTries(self):
        return self.tries