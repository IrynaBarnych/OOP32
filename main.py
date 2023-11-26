"""Завдання 1
Задайте метаклас, що автоматично додає
додатковий функціонал до всіх класів, що його
використовують."""

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct["hello"] = lambda self: print(f"Hello from {self.__class__.__name__}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass = MyMeta):
    attr = 10
    def metod(self):
        pass

print(dir(MyClass))
obj = MyClass()
print(obj.attr)
obj.hello()
