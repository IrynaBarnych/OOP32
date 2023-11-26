#Завдання 3
#Реалізуйте метаклас, що забороняє спадкування від
#певних класів чи змінює порядок спадкування.

class MyMeta(type):
    def __new__(cls, name, bases, dct):

        def hello(self):
            print(f"Hello from {self.__class__.__name__}")

        dct["hello"] = hello
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    attr = 10

    def method(self):
        pass


print(dir(MyClass))
obj = MyClass()
print(obj.attr)
obj.hello()


