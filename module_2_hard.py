n = int(input('Введите число от 3 до 20: '))
if n in range(3, 21):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += f'{i}{j}'
                continue
    print(result)

else:
    print('Некорректное число, попробуйте еще раз!')
