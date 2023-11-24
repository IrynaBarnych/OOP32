"""Завдання 2
Створіть метаклас, що перевіряє наявність певних
атрибутів у всіх класах, які використовують цей
метаклас."""


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # перелік атрибутів, які мають бути в класі
        required_attributes = ['attr1', 'attr2']

        # перевіряємо, чи всі обов'язкові атрибути присутні в dct
        for i in required_attributes:
            if i not in dct:
                raise AttributeError(f"Клас повинен мати обов'язковий атрибут: {i}")

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    attr1 = 10
    attr2 = 100
    # attr3 = "Hello!"

print(
    dir(MyClass))
obj = MyClass()
print(obj.attr1)
