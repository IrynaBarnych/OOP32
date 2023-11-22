a = 1
print(type(a))
print(type(type))
class MyParentClass1: pass
class MyParentClass2: pass
def summa(self):
    return  sum(range(10))

MyClass = type("MyClass", (MyParentClass1, MyParentClass2), {"x": 2, "y": 5,
                                                             "my_metod": lambda self: "Це метод класу",
                                                             "summa":summa})
obj = MyClass()
print(obj.x)
print(obj.y)
print(obj.my_metod())
print(MyClass.__mro__)
print(obj.summa())

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #маніпуляція з класом
        dct["attr"] = 100
        print(name)
        print(bases)
        print(dct)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    attr = 10
    def metod(self):
        pass
print(dir(MyClass))
obj = MyClass()
print(obj.attr)

###кешування
"""Метаклас для кешування результатів методів класу:
 Реалізуйте метаклас, який автоматично кешує
 результати виклику методів класу для підвищення швидкодії."""


class Cached(type):
    def __new__(cls, name, bases, dct):
        cache = {}

        def wrap_method(method):
            def wrapped(*args, **kwargs):
                cache_key = (method.__name__, args, frozenset(kwargs.items()))
                if cache_key not in cache:
                    cache[cache_key] = method(*args, **kwargs)
                print(cache)
            return wrapped
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                dct[attr_name] = wrap_method(attr_value)
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Cached):
    def calculate(self, x):
        return print(f"Розрахунок для {x} - {x ** 2}")
obj = MyClass()
obj.calculate(5)
obj.calculate(100)
obj.calculate(120)
