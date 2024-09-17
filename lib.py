#Программа, которая принимает на вход N списков и возвращает количество одинаковых элементов в них

def count_common_elements(lists):
    # Преобразуем первый список в множество
    common_elements = set(lists[0])

    # Перебираем остальные списки и находим пересечение
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)

# Ввод данных от пользователя
N = int(input("Введите количество списков: "))
lists = []

for i in range(N):
    lst = input(f"Введите элементы списка {i + 1}, разделенные пробелом: ").split()
    lists.append(lst)

# Подсчет одинаковых элементов
result = count_common_elements(lists)
print(f"Количество одинаковых элементов: {result}")
