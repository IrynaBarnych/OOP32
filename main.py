# Завдання 3
# Реалізуйте метаклас, що забороняє спадкування від певних класів чи змінює порядок спадкування.


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # перелік атрибутів, які мають бути в класі
        required_attributes = ['attr1', 'attr2']

        # перевіряємо, чи всі обов'язкові атрибути присутні в dct
        for i in required_attributes:
            if i not in dct:
                raise AttributeError(f"Клас повинен мати обов'язковий атрибут: {i}")

        # кортеж заборонених класів
        forbidden_classes = (ForbiddenBaseClass1, ForbiddenBaseClass2)

        # перевіряємо, чи жоден з заборонених класів не є в списку базових класів
        if any(forbidden_class in bases for forbidden_class in forbidden_classes):
            raise TypeError(f"Заборонено спадкування від певних класів: {forbidden_classes}")

        return super().__new__(cls, name, bases, dct)


class ForbiddenBaseClass1:
    pass


class ForbiddenBaseClass2:
    pass


class MyClass(metaclass=MyMeta):
    attr1 = 10
    attr2 = 100
    # attr3 = "Hello!"


print(dir(MyClass))
obj = MyClass()
print(obj.attr1)

