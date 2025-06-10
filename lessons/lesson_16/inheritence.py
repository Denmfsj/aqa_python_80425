class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color


    def __str__(self):
        return f'{self.animal_class} with name {self.name}, color - {self.color}'


class Cat(Animal):

    animal_class = 'CAT'

    def __init__(self, name, color, q_mustash: int):
        super().__init__(name, color)
        self.q_mustash = q_mustash


    @staticmethod
    def make_sound():
        print('Mrrrr....')


class Dog(Animal):

    animal_class = 'DOG'

    def __init__(self, name, color, sub_animals: bool):
        Animal.__init__(self, name, color)
        self.sub_animals = sub_animals

    @staticmethod
    def make_sound():
        print('Grrr....')


class CatDog(Dog, Cat):
    animal_class = 'CatDog'

    def __init__(self, name, color, q_mustash, sub_animals):

        Dog.__init__(self, name, color, sub_animals)
        Cat.__init__(self, name, color, q_mustash)

    @staticmethod
    def make_sound():
        Cat.make_sound()
        Dog.make_sound()


print(CatDog.__mro__)

cat_dog = CatDog('catdog_name', 'white', q_mustash=8, sub_animals=False)



print(cat_dog)
cat_dog.make_sound()




