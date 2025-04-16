import json

# Базовый класс для сотрудника
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self):
        print(f"{self.name} работает как {self.role}.")

# Специфический класс для хранителей животных
class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Хранитель животных")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Специфический класс для ветеринаров
class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Класс животного
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

# Класс зоопарка
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []      # список животных
        self.employees = []    # список сотрудников

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

    # Сохранение данных о зоопарке в файл
    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "animals": [{"name": animal.name, "species": animal.species} for animal in self.animals],
            "employees": [{"name": emp.name, "role": emp.role} for emp in self.employees]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные о зоопарке сохранены в {filename}")

    # Загрузка данных о зоопарке из файла
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.name = data['name']
            self.animals = [Animal(animal['name'], animal['species']) for animal in data['animals']]
            self.employees = [Employee(emp['name'], emp['role']) for emp in data['employees']]
            print(f"Данные о зоопарке загружены из {filename}")
        except FileNotFoundError:
            print("Файл не найден, создаём новый зоопарк.")

# === Демонстрация работы ===

# Создаём зоопарк
my_zoo = Zoo("Сафари Парк")

# Добавляем животных и сотрудников
lion = Animal("Лев", "Хищник")
elephant = Animal("Слон", "Травоядное")
my_zoo.add_animal(lion)
my_zoo.add_animal(elephant)

keeper = ZooKeeper("Анна")
vet = Veterinarian("Иван")
my_zoo.add_employee(keeper)
my_zoo.add_employee(vet)

# Показываем всех
my_zoo.show_all_animals()
my_zoo.show_all_employees()

# Сохраняем данные в файл
my_zoo.save_to_file("zoo_data.json")

# Загружаем данные из файла
new_zoo = Zoo("Парк дикой природы")
new_zoo.load_from_file("zoo_data.json")
new_zoo.show_all_animals()
new_zoo.show_all_employees()
