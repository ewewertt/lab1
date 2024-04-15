##Лабораторная работа №1 Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран лексемы по определенному правилу. Лексемы разделены пробелами. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
##Вариант 4.
##Натуральные простые числа, не превышающие 1 000, у которых средняя цифра равна 4. Минимальное и максимальное число выводятся прописью.

digitsList = {
    '0': "ноль", '1': "один", '2': "два", '3': "три",
    '4': "четыре", '5': "пять", '6': "шесть", '7': "семь",
    '8': "восемь", '9': "девять"
}
inputFilename = 'input.txt'
def isPrime(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
def middleFour(num):
    num_str = str(num)
    mid_index = len(num_str) // 2
    return num_str[mid_index] == '4' if len(num_str) % 2 != 0 else num_str[mid_index - 1] == '4'
primesMidFour = []
def digitToWord(number):
    return ' '.join(digitsList[digit] for digit in str(number))
def digitToWord(number):
    return ' '.join(digitsList[digit] for digit in str(number))
def processFile(inputFilename, block_size=1024):
    minPrime = maxPrime = None
    with open(inputFilename, 'r') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            numbers = block.split()
            for num_str in numbers:
                try:
                    num = int(num_str)  
                except ValueError:
                    continue 
                if isPrime(num) and middleFour(num):
                    print(digitToWord(num))
                    if minPrime is None or num < minPrime:
                        minPrime = num
                    if maxPrime is None or num > maxPrime:
                        maxPrime = num
    return minPrime, maxPrime
inputFilename = 'input.txt'
minPrime, maxPrime = processFile(inputFilename)
if minPrime is not None and maxPrime is not None:
    print("Минимальное: ", digitToWord(minPrime))
    print("Максимальное: ", digitToWord(maxPrime))
else:
    print("Простых чисел с цифрой 4 посередине не найдено.")
