"""Завдання 2"""
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #перелік атрибутів
        required_attributes = ['attr1', "attr2"]
        for i in dct:
            raise AttributeError(f"В класі {name} повинен бути тільки {i} атрибут")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass = MyMeta):
    attr1 = 10
    attr2 = 100
    attr3 = "Hello!"

print(dir(MyClass))
obj = MyClass()
print(obj.attr)
obj.hello()
