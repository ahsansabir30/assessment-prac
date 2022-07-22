def endsPy(string):
    new_string = string.lower()
    if new_string[-2:] == 'py':
        return True
    return False

def one(items):
    empty_dictionary = {}
    for item in items:
        print(item)
        empty_dictionary[item] = items.count(item)
        print(empty_dictionary)
    return empty_dictionary

def two(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return False

import math
def three(num):
    type = math.sqrt(num)
    if (type-int(type)) == 0:
        return num
    else:
        while num > 0:
            type = math.sqrt(num)
            if (type-int(type)) == 0:
                return num
                break
            else:
                num = num - 1

def four(a, b):
    if b == 0:
        return a
    return four(b, a%b)

def five(string):
    new_string = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in string:
        if char == ' ':
            new_string.append(' ')
        elif char in ['1','2','3','4','5','6','7','8','9','0']:
            new_string.append(char)
        else:
            index = alphabet.index(char)
            new_char = alphabet[index-1]
            new_string.append(new_char)
    return ''.join(new_string)
