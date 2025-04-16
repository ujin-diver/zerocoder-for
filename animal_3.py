# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

# Подклассы с переопределённым методом make_sound
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} щебечет!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит!")

# Функция демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создание списка животных
animals = [
    Bird("Воробей"),
    Mammal("Лев"),
    Reptile("Уж"),
    Bird("Попугай"),
    Mammal("Медведь")
]

# Вызов функции
animal_sound(animals)
