
text = ['  + -- + - + -  ',
        '  + --- + - +  ',
        '  + -- + - + -  ',
        '  + - + - + - +  ']

l = []
for i in text:
    l.append(
        chr(int((i.strip().replace(' ', '')).replace('+', '1').replace('-', '0'), 2)))

print(''.join(l))

''.join([chr(int((i.strip().replace(' ', '')).replace(
    '+', '1').replace('-', '0'), 2)) for i in text])

s = [i.strip().replace(' ', "").replace('+', '1').replace('-', '0')
     for i in text]

l = ''.join(list(map(lambda x: chr(int(x, 2)), s)))
print(l)


def f(x):
    return chr(int(x, 2))


m = ''.join(list(map(f, s)))
print(m)
