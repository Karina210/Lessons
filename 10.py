def main():
# Работа с файлами
#    file = open("files/file.txt") #относительный путь, если написать ./file.txt, но он равен и file.txt
#    print(file)
#    file.close() #закрывать надо после себя


#Вывод содержимого файла
   # file = open("files/file.txt")
   # print(file.readlines())
   # file.close()

# Построчное чтение (выведет все с файла на в отдельных строках)
#     file = open('files/file.txt')
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)
#     file.close()


# вывести:
#     file = open("files/file.txt")
#     lines = []
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         lines.append(line)
#
#
#     file.close()
#
#     print(lines[1]) #Первую строку
#     print(lines[-1])  #Последнюю строку
#     print(lines[::2])  #выведет 1 и 3 строку
#     print(lines[:])  #весь файл


# Чтение всех строк файлов
#     file = open("files/file.txt")
#     print(file.readlines())


#Чтение всех строк файла с помощью with
    # with open("files/file.txt") as file:
    #     for line in file.readlines():
    #         print(line)

#запись в файл в конце файла. Можно записать и список (['fghf\n', 'jfndf'])
    # with open("files/file.txt", "a") as file:
    #     file.writelines(['\nquertn\n', 'fhv'])


    # Запись в файл в начало(заменяет все на то, что написано тут)
    # with open("files/file.txt", "w") as file:
    #  file.writelines(['\nquertn\n', 'fhv'])


    # перезапись с 1 файла во второй
    file_in = open("files/file.txt", 'r')
    file_out = open("files/file2.txt", 'w')
    file_out.write(file_in.read())


    # 10.04 но не получилось
    # file_in = open("files/file.txt")
    # res_a = file_in.replace(0, 1)
    # file_in = open("files/file.txt", 'r')
    # file_out = open("files/file2.txt", 'w')
    # file_out.write(file_in.read())



if __name__ == '__main__':
    main()



