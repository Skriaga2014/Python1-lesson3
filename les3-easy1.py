def my_round(number, ndigits):
    number = str(number)                                                    #number преобразуется в строку
                                                                            #(на случай, если функции передано число)
    number = number.split(".")                                              #Разбиваем число на ДО точки и ПОСЛЕ.
    if int(ndigits) >= len(number[1]):                                      #Если ndigits >= длины числа после точки:
        return number[0] + "." + number[1]                                  #Вернуть введенное число number
    if int(number[1][int(ndigits)])>=5:                                     #Иначе если за цифрой ndigits цифра >=5:
        a = float(number[0] + "." + str(int(number[1][0:int(ndigits)])+1))  #то урезаем число после точки до ndigits,
                                                                            #к числу после точки прибавляем 1.
        if len(str(int(number[1][0:int(ndigits)])+1)) > len(str(int(number[1][0:int(ndigits)]))):
            a = float(str(int(number[0])+1) + ".0")                         #Если число после точки увеличилось в длине,
                                                                            #тогда к числу до точки прибавляем 1,
                                                                            #а число после точки обнуляем.
                                                                            #Если длина числа после точки не увеличилась,
                                                                            #объединяем число до точки с точкой и числом
                                                                            #после точки, получаем сокращенное число!
        return a                                                            #Возвращаем это число.
    a = float(number[0] + "." + str(int(number[1][0:int(ndigits)])))        #Если за цифрой ndigits стоит цифра <5:
                                                                            #то урезаем число после точки до ndigits,
                                                                            #объединяем число до точки с точкой и числом
                                                                            #после точки, получаем сокращенное число!
    return a                                                                #Возвращаем это число.


a = input("Введите дробное число (при английской раскладке клавиатуры): ")
b = input("До какого знака после запятой следует округлить: ")

print(my_round(a, b))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


