# 技巧的写法

# 解读：
# k = {b: i for i, b in enumerate(B)}
# You create hashmap of indexes of elements in B, because you are going to ask for it everytime when sorting. 
# So in case you have something like [2,2,2,2,2,2,2,1] you won't go and perform same index search everytime.

# return sorted(A, key=lambda a: k.get(a, 1000 + a))
# you are sorting initial list A with key function that will get index of element in A from hashmap that you already created 
# and in case it's not there it will add 1000 to the element itself so it will put elements that are in A but not in B after all the elements in resulting list. 
# You can do it as you know that 0 <= arr1[i], arr2[i] <= 1000


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {v: k for k, v in enumerate(arr2)}
        return sorted(arr1, key = lambda i: order.get(i, 1000 + i))