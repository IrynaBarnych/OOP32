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
