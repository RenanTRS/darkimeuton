palavra = str(input('Digite seu nome ou apelido: ')).upper().strip().split()[0]

qtd = len(palavra)
p = []

#for logic
for c in range(0, qtd):
    if palavra[c] == 'A':
        p.append(4)
    elif palavra[c] == 'B':
        p.append(8)
    elif palavra[c] == 'G':
        p.append(6)
    elif palavra[c] == 'E':
        p.append(3)
    elif palavra[c] == 'I':
        p.append(1)
    elif palavra[c] == 'O':
        p.append(0)
    elif palavra[c] == 'S':
        p.append(5)
    elif palavra[c] == 'T':
        p.append(7)
    elif palavra[c] == 'Z':
        p.append(2)
    else:
        p.append(palavra[c])

for x in p: #varrer array
    print(x, end='')

print('') #break line
