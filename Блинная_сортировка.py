def flip(arr, i):
    """Переворачивает массив от 0 до i включительно."""
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    """Находит индекс максимального элемента в первых n элементах."""
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
  
    n = len(arr)
    
    # Начинаем с полного массива и уменьшаем размер на каждом шаге
    curr_size = n
    while curr_size > 1:
        # Находим индекс максимального элемента
        max_idx = find_max(arr, curr_size)
        
        # Если максимальный элемент не на своем месте
        if max_idx != curr_size - 1:
            # Переворачиваем до максимального элемента
            flip(arr, max_idx)
            # Переворачиваем весь подмассив
            flip(arr, curr_size - 1)
        
        curr_size -= 1
    
    return arr

# Пример использования
if __name__ == "__main__":
    arr = [23, 10, 20, 11, 12, 6, 7]
    print("Блинная сортировка:")
    print("Исходный массив:", arr)
    sorted_arr = pancake_sort(arr.copy())
    print("Отсортированный массив:", sorted_arr)
    print()
