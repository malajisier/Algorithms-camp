import collections
a = [2, 1, 3, 4, 6, 6, 1, 1, 2]
b = collections.Counter(a)
print(b, len(b))
print(b.pop(1))
print(b)
