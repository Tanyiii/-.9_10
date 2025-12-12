import math

def jump_search(arr, x):

    n = len(arr)
    
    # Определяем размер прыжка
    step = int(math.sqrt(n))
    
    # Находим блок, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Элемент не найден
    
    # Линейный поиск в найденном блоке
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    
    return -1  # Элемент не найден

# Пример использования
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    x = 55
    
    print("Поиск скачками:")
    print("Массив:", arr)
    print("Ищем элемент:", x)
    
    result = jump_search(arr, x)
    
    if result != -1:
        print(f"Элемент найден на позиции {result}")
    else:
        print("Элемент не найден")
    print()
