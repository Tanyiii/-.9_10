def binary_search(arr, left, right, x):
    """Вспомогательная функция: бинарный поиск"""
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def exponential_search(arr, x):

    n = len(arr)
    
    # Если искомый элемент - первый
    if arr[0] == x:
        return 0
    
    # Экспоненциально увеличиваем диапазон
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    
    # Выполняем бинарный поиск в найденном диапазоне
    return binary_search(arr, i // 2, min(i, n - 1), x)

# Пример использования
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 45, 50, 60, 70, 80, 90, 100]
    x = 45
    
    print("Экспоненциальный поиск:")
    print("Массив:", arr)
    print("Ищем элемент:", x)
    
    result = exponential_search(arr, x)
    
    if result != -1:
        print(f"Элемент найден на позиции {result}")
    else:
        print("Элемент не найден")
    print()
