def quick_sort(arr):
    n = len(arr)
    low, high = 0, n - 1
    pivot = arr[0]

    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        low += 1

        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
        high -= 1
    
    
