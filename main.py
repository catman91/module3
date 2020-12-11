# Задача #1: множественная форма числительных

# Инициализируем функцию plural_form с 4 аргументами 

def plural_form (counter, first, second, third):

# Инициализируем переменные last(2), преобразовывая ее в строку и делаем срез 1 и 2 символа с конца
    
    last = str (counter)[-1]
    last2 = str (counter)[-2:]
    if last == '1' and counter != 11:
        return f'{counter} {first}'
    elif int(last) in [2, 3, 4] and int(last2) not in [12, 13, 14]:
        return f'{counter} {second}'
    return f'{counter} {third}'

# Проверяем работу функции 

print ('Задача #1: множественная форма числительных')
print (plural_form (1, 'яблоко', 'яблока', 'яблок'))
print (plural_form (2, 'яблоко', 'яблока', 'яблок'))
print (plural_form (11, 'студент', 'студента', 'студентов'))
print (plural_form (15, 'студент', 'студента', 'студентов'))
print (plural_form (3, 'студент', 'студента', 'студентов'))

# Задача #2: FizzBuzz

# Cоздаем пустой списк для будущей итерации

list_sum = []

# Итерируемся в пределах значений от 1 000 до 20 000 
# с условием нулевого нулевого остатка от деления на 3 и на 5
# при выполнении условия - добавляем в список list_sum

for i in range(1000, 20001):
    if i % 3 == 0 and i % 5 == 0:
        list_sum.append(i)

# Суммируем полученные значения в списке list_sum и выводим результат

sum = 0
for i in list_sum:
    sum += i
print ('Задача #2: FizzBuzz: ')
print ('{:,}'.format(sum).replace(',', ' '))
             
