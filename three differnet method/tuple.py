from string import ascii_uppercase as l


def hello():
    result = ()
    for i in range(len(l)):
        h = l[i:] + l[:i]
        result = result + (h,)
    return result


def encryption(e):
    for i in range(len(a)):
        if a[i] == ' ':
            e = e + (' ',)
        else:
            e = e + (list[(alphabets.index(b[i % len(b)]))][alphabets.index(a[i])],)
    return e


def decryption(f):
    for i in range(len(a)):
        if a[i] == ' ':
            f = f + (' ',)
        else:
            f = f + (alphabets[list[(alphabets.index(b[i % len(b)]))].index(a[i])],)
    return f


list = ()
for i in hello():
    list = list + (i,)

alphabets = (
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
a = input("Write a word: ").upper()
b = input("Write a key: ").upper()
e, f = (), ()

person = input("encryption - 1   decryption - 2\nanswer: ")
if person == '1':
    print(encryption(e))
    for i in encryption(e):
        print(i,end='')

elif person == '2':
    print(decryption(f))
    for i in decryption(f):
        print(i,end='')