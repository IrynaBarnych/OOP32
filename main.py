a = 1
print(type(a))
print(type(type))
class MyParentClass1: pass
class MyParentClass2: pass
MyClass = type("MyClass", (MyParentClass1, MyParentClass2), {"x": 2, "y": 5, "my_metod": lambda self: "Це метод класу"})
obj = MyClass()
print(obj.x)
print(obj.y)
print(obj.my_metod())
print(MyClass.__mro__)
