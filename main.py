#Завдання 1
# Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct["hello"] = lambda self: print(f"Hello from {self.__class__.__name__}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    attr = 10

    def method(self):
        pass

print(dir(MyClass))
obj = MyClass()
print(obj.attr)
obj.hello()


