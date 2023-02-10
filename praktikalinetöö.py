import math
from random import * 

#1
def арифметическая(a, b, операция):
    if операция =='+':
        return a+b
    elif операция =='-':
        return a - b
    elif операция =='*':
        return a * b
    elif операция =='/':
        return a/b
    else:
        return "Неизвестная операция"
результат=арифметическая(2, 3, '+')
print(результат)
результат=арифметическая(2, 3, '-')
print(результат) 
результат=арифметическая(2, 3, '*')
print(результат)
результат=арифметическая(2, 3, '/')
print(результат)
результат=арифметическая(2, 3, '**')
print(результат) 

#2
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#3
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal =math.sqrt(2) * side
    return perimeter, area, diagonal


#4
def season(месяц):
    if месяц in [12, 1, 2]:
        return "зима"
    elif месяц in [3, 4, 5]:
        return "весна"
    elif месяц in [6, 7, 8]:
        return "лето"
    elif месяц in [9, 10, 11]:
        return "осень"
    else:
        return "Неверный номер месяца"

#5
def bank(a, years):
    for i in range(years):
        a *= 1.1
    return a

#6
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#7
def date(day, month, year):
    if month < 1 or month > 12:
        return False
    if year < 1:
        return False
    if day < 1:
        return False
    if (month == 2 and day > 29) or (month == 2 and day > 28 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
        return False
    if (month in [4, 6, 9, 11] and day > 30) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31):
        return False
    return True
#8
def XOR_cipher(string, key):
    result = ""
    for i, char in enumerate(string):
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result
def XOR_uncipher(encrypted_string, key):
    return XOR_cipher(encrypted_string, key)