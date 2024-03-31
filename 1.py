# d1 = {'apple': 1, 'Banana': 2, 'Pears': 3}
# # Возвращает список ключей, отсортированный по значениям
# print(sorted(d1.values()))

class MyClass:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        # Магический метод __lt__ (less than) для сравнения объектов
        return self.value < other.value


# Создаем список объектов класса MyClass
objects = [MyClass(4), MyClass(1), MyClass(7), MyClass(2)]

# Сортируем список объектов
sorted_objects = sorted(objects, key=lambda x: x.value)

# Выводим отсортированный список
for obj in sorted_objects:
    print(obj.value)

print(objects[1].value)