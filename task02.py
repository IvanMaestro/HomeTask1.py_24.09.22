# 2. Напишите программу для. 
# проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат. 
# (¬ отрицание, ∧ и, ∨ или)

# Автоматический перебор
for x in range(3):
        for y in range(3):
            for z in range(3):
                print(not (x or y or z) == (not x and not y and not z))
                print(f'x:{x}, y:{y}, z:{z}')

# Проверка с пользовательского ввода
# x = float(input('Введите X: '))
# y = float(input('Введите Y: '))
# z = float(input('Введите Z: '))

# print(not (x or y or z) == (not x and not y and not z))
