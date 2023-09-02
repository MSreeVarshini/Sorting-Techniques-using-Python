# Bubble Sort
'''Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Here are the complexities of Bubble Sort in Python:

1. Time Complexity:
   - Worst-case time complexity: O(n^2)
   - Average-case time complexity: O(n^2)
   - Best-case time complexity: O(n)

   Bubble Sort has a quadratic time complexity, meaning it has to perform n^2 comparisons and swaps in the worst and average cases. The best-case time complexity occurs when the list is already sorted, and no swaps are needed, resulting in a linear time complexity of O(n).

2. Space Complexity:
   - Space complexity: O(1)

   Bubble Sort sorts the elements in place, meaning it doesn't require additional memory allocation that scales with the size of the input. Its space complexity is constant, O(1).

3. Stability:
   - Bubble Sort is a stable sorting algorithm. This means that when two elements have equal values, their relative order remains unchanged after sorting.

Bubble Sort is generally not recommended for large datasets because of its poor performance in comparison to more efficient sorting algorithms like Quick Sort or Merge Sort. However, it is easy to understand and implement, making it suitable for educational purposes and small datasets where efficiency is not a significant concern.
'''

def bubbleSort(read):

    for i in range(len(read)):
        for j in range(i, len(read)):
            if read[i] > read[j]:
                read[i], read[j] = read[j], read[i]

print("Enter the elements: ")
read = list(map(int, input().split()))
print("Elements before sorting...")
print(read)
print("Elements after sorting...")
bubbleSort(read)
print(read)