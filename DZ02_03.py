#  Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.   

N = int(input("Введите число = "))
stepen, sum, count = 2, 0, 0
while stepen ** count <= N:
    sum = stepen ** count
    print(f" {sum}", end="")
    count += 1