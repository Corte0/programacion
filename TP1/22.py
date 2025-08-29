s = 'qwertyuiopasdfghjklzxcvbAEUnm'

vocales = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vocales += 1

print(f'Numero de vocales: {vocales}')

