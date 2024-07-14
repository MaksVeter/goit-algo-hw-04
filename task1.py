import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def tim_sort(arr):
    return sorted(arr)

def measure_time(sort_function, arr):
    def wrapper():
        sort_function(arr.copy())
    return timeit.timeit(wrapper, number=1)

data_sizes = [1000, 2000, 5000, 10000]
results = { "insertion_sort": [], "merge_sort": [], "tim_sort": [] }

for size in data_sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    
    time_insertion = measure_time(insertion_sort, data)
    time_merge = measure_time(merge_sort, data)
    time_tim = measure_time(tim_sort, data)
    
    results["insertion_sort"].append((size, time_insertion))
    results["merge_sort"].append((size, time_merge))
    results["tim_sort"].append((size, time_tim))

for key, value in results.items():
    print(f"\n{key}:")
    for size, time in value:
        print(f"Size: {size}, Time: {time:.6f} seconds")
