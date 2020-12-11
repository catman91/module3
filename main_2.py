# Задача #3: Последовательность Фибоначчи   

fib1 = fib2 = 1
fibb = []
while True:
    if fib1 >= 10000000:
        break
    fibb.append(fib1)
    fib1, fib2 = fib2, fib1 + fib2

print (f'Количество элементов в последовательности: {len(fibb)}')
evens = [i for i in fibb if i % 2 == 0]
print (f'Cумма всех четных элементов: {sum(evens)}')
print (f'Все четные элементы: {evens}')
print(f'Предпоследнее число последовательности: {fibb[-2]}')
