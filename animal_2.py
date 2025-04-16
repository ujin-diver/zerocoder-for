# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест пищу.")

# Подкласс для птиц
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не умеет летать.")

# Подкласс для млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, has_fur=True):
        super().__init__(name, age)
        self.has_fur = has_fur

    def make_sound(self):
        print(f"{self.name} рычит или издает млекопитающее звучание.")

# Подкласс для рептилий
class Reptile(Animal):
    def __init__(self, name, age, is_venomous=False):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} шипит.")

# Создаем животных
parrot = Bird("Кеша", 2)
tiger = Mammal("Шерхан", 5)
snake = Reptile("Каа", 3, is_venomous=True)

# Проверка работы
parrot.make_sound()
parrot.fly()

tiger.make_sound()
tiger.eat()

snake.make_sound()
print(f"Ядовитая? {'Да' if snake.is_venomous else 'Нет'}")
