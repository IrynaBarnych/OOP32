# Завдання 3
# Реалізуйте метаклас, що забороняє спадкування від певних класів чи змінює порядок спадкування.


class Meta(type):
    forbidden_classes = []

    def __new__(cls, name, bases, dct):
        for forbidden_class in cls.forbidden_classes:
            if forbidden_class in bases:
                raise TypeError(f"Спадкування від класу '{forbidden_class.__name__}' не дозволено.")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    attr = 10

class ForbiddenClass:
    pass

Meta.forbidden_classes.append(ForbiddenClass)

if ForbiddenClass in Meta.forbidden_classes:
    print(f"Спадкування від класу '{ForbiddenClass.__name__}' не дозволено.")

class AnotherClass(MyClass):
    pass
