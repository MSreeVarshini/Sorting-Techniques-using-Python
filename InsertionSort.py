# Insertion Sort 
'''Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. Here's a basic overview of the complexity analysis for Insertion Sort in Python:

1. Time Complexity:

   - WorstCase: In the worst case, when the input array is sorted in reverse order, and each element needs to be moved to the beginning of the sorted section, the time complexity is O(n^2), where 'n' is the number of elements in the array.

   - BestCase: In the best-case scenario, when the input array is already sorted, the time complexity is O(n). This is because, in each pass, only one comparison is needed to determine that the current element is already in its correct position.

   - AverageCase: The average-case time complexity of Insertion Sort is also O(n^2). It performs roughly on par with the worst-case scenario for random or unsorted data.

2. Space Complexity:

   - The space complexity of Insertion Sort is O(1), which means it sorts the array in-place and does not require any additional memory allocation proportional to the size of the input.

3. Stability:

   - Insertion Sort is a stable sorting algorithm. This means that it maintains the relative order of equal elements in the sorted array. If you have two equal elements in the input, the one that appears earlier will still be earlier in the sorted array.

4. Adaptive:

   - Insertion Sort can be adaptive, meaning that its performance improves when the input is partially sorted. In the best-case scenario (already sorted input), it runs in linear time.

In summary, while Insertion Sort is not the most efficient sorting algorithm for large datasets, it can be useful for small datasets or as part of more advanced sorting algorithms like Timsort, which uses a combination of Insertion Sort and Merge Sort to achieve better performance.
'''


def insertionSort(read):
    
    for i in range(0, len(read)):
        key = read[i]
        j = i - 1
        while j >= 0 and key < read[j]:
            read[j+1] = read[j]
            j -= 1
        read[j+1] = key

print("Enter the elements: ")
read = list(map(int, input().split()))
print("Elements before sorting...")
print(read)
print("Elements after sorting...")
insertionSort(read)
print(read)