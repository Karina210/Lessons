# from functools import reduce

# фильтрует сначала все числа и выбирает кратные 3, а потом перемножает их
b = list(filter(lambda x: x % 3 == 0,[1,2,3,4,5,6]))
# result = reduce(lambda a, x: a * x, b)
# print(result)


#  посчитает сумму
a = lambda x, y: x + y
# print(a(32, 54))


# напишет привет и имя
b = lambda x: f'Hello {x}'
# print(b("karina"))


# выведет список приветствия
c = lambda x: [b(name) for name in x]
# print(c(["karina", "ilya"]))


# сделает сткокой этот список и они будут в кавычках
# print(list(map(lambda x: str(x), [1, 2, 3])))


# выведет имя в котором есть буква к
# print(list(filter(lambda x: "k" in x, ["karina", "marina"] )))




# def a(func):
#     def wrap():
#       print('it is my code')
#       func()
#     return wrap
# @a
# def h():
#     print('hello')
# @a
# def b():
#     print('bye')

# decorator_h = a(h)
# decorator_h()

# h()
# b()

