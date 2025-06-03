class Animal:

    def __init__(self, name):
        self.name = name

    @classmethod
    def sit(cls):  # method
        print('Sitting....')


class Dog(Animal):

    type_of_animal = 'dog'

    @classmethod
    def make_noise(cls, ):  # method
        print('Rrrrr....')
        print(cls.type_of_animal)

    def go_here(self, place):
        self.make_noise()
        print(f'{self.name} is walking...')
        self.sit(place)

    @classmethod
    def sit(cls, place):  # class method
        print(f'Dog is Sitting at {place}....')


class Cat(Animal):

    type_of_animal = 'cat'

    @classmethod
    def make_noise(cls):  # method
        print('Miay....')



print(Dog.type_of_animal)
Dog.make_noise()

brovko = Dog('brovko')  # instance, екземпляр
brovko.sit('yard')


# naida = Dog()  # instance, екземпляр
# aria = Cat()
#
# # brovko.make_noise()
# # aria.make_noise()
# naida.go_here()
#
# my_name = 'Denys'
#
# my_name.upper()
# [1,2].append(2)

# print(my_name + ' Mer')
# print(1+5)

# [1,2,3].pop()
# {1:2, 4:5}.pop(4)
# {1,2,3,4,5}.pop()