class Animal:
    """
    Animal Class
    """
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, Exhale')


class Fish(Animal):
    """
    Fish class inheriting methods and attribues from Animal Class
    """

    def __init__(self):
        super().__init__() #initializes what in Animal class to fish class

    def breathe(self):
        super().breathe() #imports what in breathe method of Animal Class to Fish Class breathe method
        #adding extra to fish class breathe method
        print('under the water')

    def swim(self):
        print(f'Moving under water')

print('Animal Class Output\n')
cow = Animal()
print(cow.num_eyes)
cow.breathe()
print('\n--------END---------\n')


print('Fish Class Output\n')
shark = Fish()
print(shark.num_eyes)
shark.breathe()
shark.swim()
print('\n--------END---------\n')