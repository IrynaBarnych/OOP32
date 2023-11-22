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

###
"""Зміна поведінки операторів класу: Створіть метаклас,
який дозволяє змінювати поведінку різних операторів
(наприклад, +, -, *, /) для об'єктів певного класу."""

# +
class OperatorOverloadMeta(type):
    def __new__(cls, name, bases, dct):
         dct["__add__"] = lambda self, other: self.add(other)
         dct["__sub__"] = lambda self, other: self.sub(other)
         dct["__mul__"] = lambda self, other: self.mul(other)
         dct["__truediv__"] = lambda self, other: self.truediv(other)
         return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=OperatorOverloadMeta):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.value + other.value if isinstance(other, MyClass) else self.value + other
    def sub(self, other):
        return self.value - other.value if isinstance(other, MyClass) else self.value - other
    def mul(self, other):
        return self.value * other.value if isinstance(other, MyClass) else self.value * other
    def truediv(self, other):
        return self.value / other.value if isinstance(other, MyClass) else self.value / other

obj1 = MyClass(10)
obj2 = MyClass(2)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)



