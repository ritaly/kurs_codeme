class Dog:
    def __init__(self, name, colour, breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def sound(self):
        print('Hau hau')

obj_dog = Dog('dyzio', 'grey', 'jamnik')

print(obj_dog.name)

obj_dog.sound()