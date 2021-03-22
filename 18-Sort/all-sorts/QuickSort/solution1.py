def quick_sort(arr):
    if len(arr) == 0 or 1: return arr
    pivot = partition(arr, 0, len(arr) - 1)
    quick_sort(arr, 0, pivot - 1)
    quick_sort(arr, pivot + 1, len(arr) - 1)

def partition(arr, le, high):
    pivot = arr[0]

    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        if low < high:
            arr[low] = arr[high]
            low += 1

        while low < high and arr[low] < pivot:
            low += 1
        if low < high:
            arr[high] = arr[low]
            high -= 1
        arr[low] = pivot
    return pivot
    
if __name__ == '__main__':
    a = [5,1,2,9,7]
    print(a)
    quick_sort(a)
    print(a)
    
