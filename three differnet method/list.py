from string import ascii_uppercase as l
def hello():
    result = []
    for i in range(len(l)):
        h = l[i:] + l[:i]
        result.append(h)
    return result

def encryption(e):
    for i in range(0, len(a)):
        if a[i] == ' ':
            e.append(' ')
        else:
            e.append(list[(alphabets.index(b[i % len(b)]))][alphabets.index(a[i])])
    return e

def decryption(f):
    for i in range(0, len(a)):
        if a[i] == ' ':
            e.append(' ')
        else:
            f.append(alphabets[list[(alphabets.index(b[i % len(b)]))].index(a[i])])
    return f

list = []
for i in hello():
    list.append(i)
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = input("write a word: ").upper()
b = input("write a key: ").upper()
e,f = [],[]

person = input("encryption - 1   decryption - 2\nanswer: ")
if person == '1':
    print(encryption(e))
    for i in e:
        print(i, end='')

elif person == '2':
    print(decryption(f))
    for i in f:
        print(i, end='')