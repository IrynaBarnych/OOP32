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
