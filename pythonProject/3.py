
# Найти номера минимального и максимального элементов первой половины списка.

list = [2, 1, 16, 4, 0, 36]
min_number = max_number = list[0]
for i in range(len(list) // 2):
    if list[i] > max_number:
        max_number = list[i]
    if list[i] < min_number:
        min_number = list[i]
print('Номер минимального элемента', list.index(min_number) + 1, 'со значением',  min_number)
print('Номер максимального элемента', list.index(max_number) + 1, 'со значением', max_number)

