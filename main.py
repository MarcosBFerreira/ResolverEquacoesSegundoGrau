print('Exemplos de expressões válidas:\n\n - 3x**2 + 12x - 9\n + 3x**2 + 12x - 9\n   3x**2 + 12x - 9\n')
expressao = str(input('Digite a expressão: '))

aux = expressao

expressao = expressao.split()



a = 0
b = 0
c = 0

if '+' not in expressao[0] and expressao[0] != '-':
    expressao.insert(0, '+')

for i in range(len(expressao)):

    try:
        if expressao[i].count('x**2'):

            a += int(f"{expressao[i-1]}{int(expressao[i].split('x**2')[0])}")
            expressao.pop(i-1)

        elif expressao[i].count('x') and expressao[i].count('x**2') is not True:

            b += int(f"{expressao[i-1]}{int(expressao[i].split('x')[0])}")
            expressao.pop(i-1)

        else:

            c += int(f"{expressao[i-1]}{int(expressao[i])}")

    except:
        pass

delta = b**2 - 4 * a * c
raiz_delta = delta ** (1/2)


if raiz_delta > 0:

    try:

        raiz1 = (-b + raiz_delta) / (2 * a)
        raiz2 = (-b - raiz_delta) / (2 * a)

    except ZeroDivisionError:

        print(f'2 * {a} = 0 e não existe divisão por 0')

    if raiz1 == -0.0:

        raiz1 = 0.0

    if raiz2 == -0.0:

        raiz2 = 0.0

    print(f"\nAs raízes de {aux} são:\n\nx' = {raiz1}\nx'' = {raiz2}")

elif raiz_delta == 0:

    try:

        raiz1 = (-b + raiz_delta) / (2 * a)

    except ZeroDivisionError:

        print(f'2 * {a} = 0 e não existe divisão por 0')

    if raiz1 == -0.0:

        raiz1 = 0.0

    print(f"\nA raiz de {aux} são:\n\nx' = {raiz1}")

else:

    print('Não existe raiz')

input('\n\nAPERTE <ENTER> PARA FECHAR O PROGRAMA')
