"""Завдання 2
Створіть метаклас, що перевіряє наявність певних
атрибутів у всіх класах, які використовують цей
метаклас."""
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #перелік атрибутів
        required_attributes = ['attr1', "attr2"]
        for i in required_attributes:
            if i not in dct:
                raise AttributeError("В класі повинен мати тільки ['attr1', 'attr2'] атрибути")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass = MyMeta):
    attr1 = 10
    attr2 = 100
    #attr3 = "Hello!"

print(dir(MyClass))
obj = MyClass()
print(obj.attr1)