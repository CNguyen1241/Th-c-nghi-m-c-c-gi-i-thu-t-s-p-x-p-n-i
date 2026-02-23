import numpy as np
import time
import heapq

SIZE = 1000000


import numpy as np
import time

def load_datasets():
    data = np.load("datasets.npz")
    return [data[key] for key in data]

datasets = load_datasets()

#QuickSort

def quicksort(arr):
    arr = arr.tolist()

    def _quicksort(a, low, high):
        if low < high:
            pivot = a[(low + high) // 2]
            i, j = low, high
            while i <= j:
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1
                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    i += 1
                    j -= 1
            _quicksort(a, low, j)
            _quicksort(a, i, high)

    _quicksort(arr, 0, len(arr) - 1)
    return arr


#HeapSort

def heapsort(arr):
    arr = arr.tolist()
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

#MergeSort

def mergesort(arr):
    n = len(arr)
    result = arr.tolist()
    temp = [0] * n
    
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)


            l_idx, r_idx = left, mid
            for k in range(left, right):
                if l_idx < mid and (r_idx >= right or result[l_idx] <= result[r_idx]):
                    temp[k] = result[l_idx]
                    l_idx += 1
                else:
                    temp[k] = result[r_idx]
                    r_idx += 1
        
        result[:] = temp[:]
        width *= 2
        
    return result




def benchmark(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr.copy())
    end = time.perf_counter()
    return end - start


def main():
    datasets = load_datasets()

    algorithms = {
        "QuickSort": quicksort,
        "HeapSort": heapsort,
        "MergeSort": mergesort,
        "Numpy Sort": lambda x: np.sort(x)
    }

    for idx, data in enumerate(datasets):
        print(f"\nDataset {idx+1}")
        for name, func in algorithms.items():
            t = benchmark(func, data)
            print(f"{name}: {t:.4f} seconds")


if __name__ == "__main__":
    main()

