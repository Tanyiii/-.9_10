def bead_sort(arr):

    if not arr:
        return []
    
    # Находим максимальное значение
    max_val = max(arr)
    
    # Создаем "абак" - матрицу бусин
    # Каждый столбец соответствует числу, каждая строка - позиции бусин
    abacus = [[0] * len(arr) for _ in range(max_val)]
    
    # Размещаем бусины (1 - есть бусина, 0 - нет)
    for i, num in enumerate(arr):
        for j in range(num):
            abacus[j][i] = 1
    
    # Применяем "гравитацию" - бусины падают вниз
    for col in range(len(arr)):
        # Считаем количество бусин в столбце
        bead_count = sum(abacus[row][col] for row in range(max_val))
        
        # Опускаем бусины
        for row in range(max_val):
            if row < bead_count:
                abacus[row][col] = 1
            else:
                abacus[row][col] = 0
    
    # Считываем результат сверху вниз
    result = []
    for col in range(len(arr)):
        # Считаем бусины в столбце
        bead_count = sum(abacus[row][col] for row in range(max_val))
        result.append(bead_count)
    
    # Так как бусины опускаются, получаем отсортированный по убыванию массив
    # Для сортировки по возрастанию нужно инвертировать
    result.reverse()
    
    return result

# Пример использования
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Сортировка бусинами:")
    print("Исходный массив:", arr)
    sorted_arr = bead_sort(arr)
    print("Отсортированный массив:", sorted_arr)
    print()
