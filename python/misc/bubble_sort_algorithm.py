'''
1. Compare each pair of adjacent elements in the list
2. If they're in the wrong order, swap them  
3. Go through the entire list doing this
4. After each complete pass, the largest element "bubbles" to the end
5. Repeat, but ignore the already-sorted elements at the end
6. Stop when you make a pass with no swaps (list is sorted)
'''

import random

array = [random.randint(1, 100) for _ in range(10)]
print("Original array:", array)

n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted array:", array)