# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

P = int(input("Введите сумму двух чисел = "))
S = int(input("Введите произведение чисел = "))
if P>S:
    print("Неправельные значения \n")
    
for x in range(P):
    for y in range(S):
        if P == x + y and S == x * y:
            print(f"первое число = {x} \nвторое число = {y} ")