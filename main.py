# Завдання 4
# Створіть метаклас, який автоматично реєструє всі
# нові класи у певному реєстрі для подальшого
# використання.

class RegistryMeta(type):
    cache = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.cache[name] = new_class
        return new_class

class MyClass1(metaclass=RegistryMeta):
    pass

class MyClass2(metaclass=RegistryMeta):
    pass

print(RegistryMeta.cache)
