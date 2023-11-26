#Завдання 3
#Реалізуйте метаклас, що забороняє спадкування від
#певних класів чи змінює порядок спадкування.

class Meta(type):
    def __init_subclass__(cls):
        new_bases_order = (BaseClass2, BaseClass1)
        cls.__bases__ = new_bases_order
        super().__init_subclass__()

class BaseClass1:
    pass

class BaseClass2:
    pass

class MyClass(metaclass=Meta):
    pass

print(MyClass.__bases__)







