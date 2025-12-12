def bucket_sort(arr):

    if len(arr) == 0:
        return arr
    
    # Определение количества корзин
    num_buckets = len(arr)
    
    # Создание корзин
    buckets = [[] for _ in range(num_buckets)]
    
    # Распределение элементов по корзинам
    for num in arr:
        index = int(num * num_buckets)  # Для чисел от 0 до 1
        if index == num_buckets:  # Крайний случай
            index -= 1
        buckets[index].append(num)
    
    # Сортировка каждой корзины
    for bucket in buckets:
        bucket.sort()
    
    # Объединение корзин
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Пример использования
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Блочная сортировка:")
    print("Исходный массив:", arr)
    sorted_arr = bucket_sort(arr)
    print("Отсортированный массив:", sorted_arr)
    print()
