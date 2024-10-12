class Cup:
    def __init__(self, liquid, volume, filled):
        self.liquid = liquid
        self.volume = volume
        self.filled = filled

    def fill(self):
        self.filled = True
        print(f'Cup of {self.liquid} is filled')

    def drink(self):
        self.filled = False
        print(f'Cup of {self.liquid} is empty.')

    def info(self):
        print(f'Cup of {self.liquid} have {self.volume} is {self.filled}')
