def ternary_search(arr, left, right, x):

    if right >= left:
        # Делим диапазон на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Проверяем, не нашли ли элемент на границах
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        
        # Определяем, в какой трети искать дальше
        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)
    
    return -1  # Элемент не найден

def ternary_search_iterative(arr, x):
    """
    Тернарный поиск (итеративная версия).
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        
        if x < arr[mid1]:
            right = mid1 - 1
        elif x > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Пример использования
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 6
    
    print("Тернарный поиск:")
    print("Массив:", arr)
    print("Ищем элемент:", x)
    
    # Рекурсивная версия
    result_recursive = ternary_search(arr, 0, len(arr) - 1, x)
    print(f"Рекурсивная версия: элемент на позиции {result_recursive}")
    
    # Итеративная версия
    result_iterative = ternary_search_iterative(arr, x)
    print(f"Итеративная версия: элемент на позиции {result_iterative}")
