msg = input('Message: ').lower()


# Using reflect method of encoding
code = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
    ' ': ' ',
    '1': '0',
    '2': '9',
    '3': '8',
    '4': '7',
    '5': '6',
    '6': '5',
    '7': '4',
    '8': '3',
    '9': '2',
    '0': '1'
}


encode = ''

for i in msg:
    x = i.replace(i, code[i])
    encode += x

print(f'Coded msg: {encode}')
