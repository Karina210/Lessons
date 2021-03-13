# class Dog: #Название класса желательно с большой
#     __name = ''
#     color = ''
#     weight = ''
#     age = ''
#     __master = True
#     adress = 'Minsk'
#
#
#     def __init__(self, name, color, weight, age):
#         self.__name = name
#         self.color = color
#         self.weight = weight
#         self.age = age
#
#
#
#     def bark(self): #селф нужен везде
#         print(f"Woof {self.__name}, color is {self.color}, weight is {self.weight}, age is {self.age}, ")
#
#
#     def rename(self, new_name): #Изменение атрибутов
#         self.__name = new_name
#
#     def set_name(self, new_name):
#         if new_name == "Qwerty":
#             return
#         self.__name = new_name
#            # return self.__name
#
#     def get_name(self, new_name):
#         return self.__name
#
#     def get_master(self) -> bool: #11.06
#         return self.__master
#
#     def get_adress(self):
#         return self.__adress
#
#     def set_adress(self, new_adress):
#         self.__adress = new_adress
#
#
#
#     # def jump(self):
#     #     print("Jump!")
#     #
#     # def run(self):
#     #     print("Run!")
#
#
# def main():
#     # dog1 = Dog()
#     # print(dog1)
#     # dog1.name = "Rax"
#     # print(dog1.name)
#     # dog1.bark()
#     # dog1.jump()
#     # dog1.run()
#     dog1 = Dog("Rax", "brown", 14, 6) #К деф инит и деф барк это и следующее
#     dog1.bark()
#     dog1.rename("Qwerty")
#     dog1.bark() #Изменение атрибутов это и вверху
#     dog1.__name = "test"
#     dog1.bark()
#     print(dog1.get_name())
#     print(dog1.adress)
#
#
# класс как тип данных
# class Point():
#     x = 0
#     y = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Line():
#     point_a = None
#     point_b = None
#
#     def __init__(self, a: Point, b: Point):
#         self.point_a = a
#         self.point_b = b
#
#     def lenght(self):
#         diff = self.point_a.y - self.point_b.y
#         if diff < 0:
#             diff = - diff
#         return diff
#
#
# def points():
#     line = Line(Point(1,2), Point(1,8))
#     print(line.lenght())




# наследование и сравнение 2-х функций
class Animal:
    name = ''
    age = 0
    master = False
    weight = 0
    height = 0

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name}, running')

    def jump(self):
        print(f'{self.name}, jumping')

    def birthday(self):
        self.age += 1

    def change_weight(self, new_weight=0):
        if not new_weight:
            new_weight = 0.2
        self.weight += new_weight

    def change_height(self, new_height=0):
        if not new_height:
            new_height = 0.2
        self.height += new_height

    def voice(self, voice): #не добавляется в инит и является пустым методом, поэтому добавляется потом в каждый класс
        print(f'{self.name}, {voice}')


class Dog(Animal):
    test = ''

    def run(self):
        if self.weight > 0.3:
            print('too fat!')
            return
        else:
            super().run()

    def bark(self):
        print(f'{self.name}, bark!')

    def jump(self, height=0):
        if height > 0.5:
            print('Dog cannot jump too height')
            return
        super(Dog, self).jump()

    def voice(self):
        super(Dog, self).voice('bark!')


class Cat(Animal):
    def meow(self):
        print(f'{self.name}, meow!')

    def voice(self):
        super(Cat, self).voice('meow!')


class Parrot(Animal):
    species = ''

    def fly(self):
        if self.weight > 0.1:
            print('Parrot cannot fly!')
            return
        print(f'{self.name}, fly!')


def main():
    dog = Dog('rax', 7, False)
    dog2 = Dog('qwertyu', 6, True)
    print(f'dog2 > dog1 :{dog2.age > dog.age}')
    dog.run()
    dog.jump()
    dog.change_height()
    dog.change_weight()
    dog.voice()
    dog.run()
    dog.weight = 8
    dog.run()
    cat = Cat('lary', 8, True)
    cat.run()
    cat.voice()
    cat.meow()
    parrot = Parrot('Max', 9, False)
    parrot.run()
    print(dir(parrot)) #выводит все об объекте



# декораторы в классах
# class Dog:
#     __name = ''
#     __master = True
#     __address = "Minsk"
#
#     def __init__(self, name, color):
#         self.__name = name
#         self.color = color
#
#     def bark(self):
#         print(f"Woof {self.__name}, color is {self.color}")
#
#     def set_name(self, new_name):
#         if new_name == "Qwerty":
#             return
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def get_master(self) -> bool:
#         return self.__master
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self, new_address):
#         print("Im here")
#         self.__address = new_address
#
#
# def main():
#     dog1 = Dog("Rax", "brawn")
#     dog1.bark()
#     dog1.set_name("Qwerty")
#     dog1.bark()
#     print(dog1.get_name())
#     print(dog1.address)
#     dog1.address = "Riga"
#     print(dog1.address)



if __name__ == '__main__':
    main()

