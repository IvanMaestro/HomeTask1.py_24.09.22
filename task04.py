# 4.Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат 
# точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))
while quarter < 1 or quarter > 4:
    print('Неверное значение. Попробуйте снова.')
    quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('Диапозон возможных координат: X > 0, Y > 0')
elif quarter == 2:
    print('Диапозон возможных координат: X < 0, Y > 0')
elif quarter == 3:
    print('Диапозон возможных координат: X < 0, Y < 0')
elif quarter == 4:
    print('Диапозон возможных координат: X > 0, Y < 0')
