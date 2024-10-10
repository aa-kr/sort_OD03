a = [1, 9, 12, 3, 7, 5, -5, 5, 15, 10, 4, 6]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insert_sort(a)
print(a)
# Результат: [-5, 1, 3, 4, 5, 5, 6, 7, 9, 10, 12, 15]