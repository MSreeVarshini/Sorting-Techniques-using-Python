# Quick Sort
'''QuickSort is a widely-used sorting algorithm known for its efficiency and average-case performance. It uses a divide-and-conquer strategy to sort an array or list of elements. The algorithm works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

QuickSort has the following time and space complexities:

1.Time Complexity:

 - Best Case: O(n log n) - The best-case scenario occurs when the pivot chosen in each step divides the input array into two roughly equal halves. In this case, the algorithm makes log₂(n) recursive calls (where n is the number of elements) and processes each element once during each call. Therefore, the best-case time complexity is O(n log n).

 - Average Case: O(n log n) - The average-case time complexity is also O(n log n). QuickSort tends to perform well on average because it often divides the array into roughly equal halves, resulting in balanced recursion.

 - Worst Case: O(n²) - The worst-case scenario occurs when the pivot chosen in each step is either the smallest or largest element in the array. This can lead to unbalanced partitions, causing QuickSort to degenerate into a worst-case time complexity of O(n²). However, this worst-case scenario is rare when using randomized pivot selection strategies or median-of-three pivot selection.

QuickSort's average and best-case time complexities make it a highly efficient sorting algorithm in practice. However, it's essential to address the worst-case scenario, which can be mitigated through randomized pivot selection or median-of-three pivot selection strategies.

2.Space Complexity:

QuickSort is an in-place sorting algorithm, which means it doesn't require additional memory for storing temporary data structures like merge sort does. However, it does have a space complexity due to its recursive nature:

1. **Space Complexity**: O(log n) - QuickSort's space complexity primarily comes from the recursion stack. In the best and average cases, the maximum depth of recursion is O(log n), which means it uses O(log n) additional memory. In the worst case, the recursion stack can go up to O(n) in depth, resulting in a worst-case space complexity of O(n).

It's important to note that this space complexity is generally considered efficient, especially when compared to algorithms like merge sort, which require additional memory for merging two sub-arrays. QuickSort's in-place nature makes it memory-efficient for practical purposes.

In summary, QuickSort is known for its efficient average and best-case time complexities of O(n log n) and its in-place nature with a space complexity of O(log n) on average. However, its worst-case time complexity of O(n²) can be improved using pivot selection strategies to ensure balanced partitioning.
'''

def quickSort(read, low, high):
    if low<high:
        pi = partition(read, low, high)
        quickSort(read, low, pi-1)
        quickSort(read, pi+1, high)

def partition(read, low, high):
    pivot = read[high]
    i = low-1
    for j in range(low, high):
        if read[j] <= pivot:
            i += 1
            read[i], read[j] = read[j], read[i]
    read[i+1], read[high] = read[high], read[i+1]
    return i+1

print("Enter the elements: ")
read = list(map(int, input().split()))
print("Elements before sorting...")
print(read)
n = len(read)
print("Elements after sorting...")
quickSort(read, 0, n-1)
print(read)    