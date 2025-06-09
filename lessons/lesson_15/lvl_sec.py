class Car:

    def __init__(self, make, model, year):
        self.make = make  # Public attribute
        self._model = model  # Protected attribute
        self.__init_year =  year
        self.__year = 2022  # Private attribute  буде зберігатись в цій змінній _Car__year


    def display_model(self):
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year

class Toyota(Car):

    def get_year(self):
        return self._Car__year


# Створення об'єкта та використання атрибутів та методів
my_car = Toyota("Toyota", "Camry")


print(my_car._model)
print(my_car.get_year())

# print(my_car.make)  # Public attribute, виведе: Toyota
# my_car.display_model()  # Protected method, виведе: Model: Camry
# my_car.update_year(2023)  # Private attribute update

