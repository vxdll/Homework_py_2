# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#Задаём список [-N, N], Рекомендую вводить n >= 5, при текущих позициях в file.txt
n = int(input("n = "))
result = []
for i in range(-abs(n), abs(n+1)):
    result.append(i)
print(result)

# считываем данные из файла file.txt
data = open("file.txt", "r")
a = result[int(data.readline())]
b = result[int(data.readline())]
c = result[int(data.readline())]
d = result[int(data.readline())]
data.close()

# считаем произведение
mult = a * b * c * d
print(f"Произведение чисел:{a},{b},{c},{d} = {mult}")



