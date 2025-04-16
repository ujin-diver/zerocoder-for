# Класс животного
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

# Класс сотрудника
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self):
        print(f"{self.name} работает как {self.role}.")

# Класс зоопарка (композиция)
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []      # список объектов Animal
        self.employees = []    # список объектов Employee

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name} ({animal.species})")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}, роль: {employee.role}")

    def show_all_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.species})")

    def show_all_employees(self):
        print("\nСотрудники зоопарка:")
        for emp in self.employees:
            print(f"- {emp.name} ({emp.role})")

# === Демонстрация работы ===

# Создаём зоопарк
my_zoo = Zoo("Сафари Парк")

# Добавляем животных
my_zoo.add_animal(Animal("Лев", "Хищник"))
my_zoo.add_animal(Animal("Слон", "Травоядное"))

# Добавляем сотрудников
my_zoo.add_employee(Employee("Анна", "Уход за животными"))
my_zoo.add_employee(Employee("Иван", "Экскурсовод"))

# Показываем всех
my_zoo.show_all_animals()
my_zoo.show_all_employees()
