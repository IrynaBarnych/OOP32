#Завдання 4
#Створіть метаклас, який автоматично реєструє всі
#нові класи у певному реєстрі для подальшого використання.

class Meta(type):
    registered_classes = {}

    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)
        cls.registered_classes[clsname] = new_class

        return new_class

class MyClass1(metaclass=Meta):
    pass

class MyClass2(metaclass=Meta):
    pass

print(Meta.registered_classes)






