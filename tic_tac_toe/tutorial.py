# class Car:
#     def __init__(self, model, brand, year):
#         self.model = model
#         self.brand = brand
#         self.year = year
#
#     def display_info(self):
#         print(f'This is a {self.model} and a popular model {self.brand} from the year {self.year}')
#
# car1 = Car('Toyota', 'Corolla', '2020')
# car2 = Car('Tesla', 'Model 3', '2023')
#
# car1.display_info()
# car2.display_info()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f'{self.name} barks and its breed is {self.breed}')

a = Animal('Some animal')
b = Dog("Buddy", 'Golden Retriever')

a.speak()
b.speak()