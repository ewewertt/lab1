digitsList = {
    '0': "ноль", '1': "один", '2': "два", '3': "три",
    '4': "четыре", '5': "пять", '6': "шесть", '7': "семь",
    '8': "восемь", '9': "девять"
}

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
for number in range(2, 1001):
    if isPrime(number) and middleFour(number):
        primesMidFour.append(number)

minPrime = min(primesMidFour) if primesMidFour else None
maxPrime = max(primesMidFour) if primesMidFour else None

def digitToWord(number):
    return ' '.join(digitsList[digit] for digit in str(number))

with open('LB1_result.txt', 'w', encoding='utf-8') as file:
    file.write("Минимальное число: " + digitToWord(minPrime) + '\n')
    file.write("Максимальное число: " + digitToWord(maxPrime) + '\n')