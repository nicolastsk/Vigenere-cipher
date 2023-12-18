from string import ascii_uppercase as l


def hello():
    result = ""
    for i in range(len(l)):
        h = l[i:] + l[:i]
        result += h
    return result


def encryption(e):
    for i in range(len(a)):
        if a[i] == ' ':
            e += ' '
        else:
            e += list[(alphabets.index(b[i % len(b)])) * 26 + alphabets.index(a[i])]
    return e


def decryption(f):
    for i in range(len(a)):
        if a[i] == ' ':
            f += ' '
        else:
            f += alphabets[list[(alphabets.index(b[i % len(b)])) * 26:].index(a[i])]
    return f


list = ''
for i in hello():
    list += i

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = input("Write a word: ").upper()
b = input("Write a key: ").upper()
e, f = "", ""

person = input("encryption - 1   decryption - 2\nanswer: ")
if person == '1':
    print(encryption(e))
elif person == '2':
    print(decryption(f))