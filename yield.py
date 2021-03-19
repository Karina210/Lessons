from random import randint
from time import sleep


#бесконечный генератор случайных чисел с условием 14.02
def create_generator(a, b, c) :
    while True:
        yield randint(a, b)
        a += c
        b += c
        sleep(1)

# if __name__ == '__main__':
#
#     for i in create_generator(0, 4, 2):
#         print(i)



#№2
def create_generator():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    # <generator object createGenerator at 0x000000>
    gen = create_generator()
    print(f'{next(gen)}!')
    print(f'{next(gen)}@')