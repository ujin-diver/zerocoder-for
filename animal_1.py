class Animal:
    def __init__(self, name, age):
        self.name = name  # имя животного
        self.age = age    # возраст животного

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self, food):
        print(f"{self.name} ест {food}.")

# Пример использования:
animal = Animal("Животное", 5)
animal.make_sound()
animal.eat("траву")
