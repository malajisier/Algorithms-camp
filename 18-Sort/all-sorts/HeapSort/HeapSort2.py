def down(arr, size, u):
    cur = u
    left, right = 2 * u, 2 * u + 1 
    if left <= size and arr[left] > arr[cur]: cur = left
    if right <= size and arr[right] > arr[cur]: cur = right
    if cur != u:
        arr[cur], arr[u] = arr[u], arr[cur]
        down(arr, size, cur)

def up(arr, u):
    while u//2 and arr[u//2] < arr[u]:
        arr[u//2], arr[u] = arr[u//2], arr[u]
        u = u//2

def heap(arr, size):
    for i in range(1, size):
        up(arr, i)
    for i in range(1, size):
        arr[1], arr[size] = arr[size], arr[1]
        size -= 1
        down(arr, size, 1)
   

if __name__ == '__main__':
    arr = [6,3,2,6,7,9,1]
    arr.append()
    heap(arr, len(arr))
    print(arr)
    
