# Merge Sort
'''Merge Sort is a comparison-based sorting algorithm known for its stability and consistent performance. Let's analyze its time and space complexity:

**Time Complexity:**

The time complexity of Merge Sort is consistent across various cases (best case, average case, and worst case), making it a reliable choice for sorting. The algorithm operates in the following manner:

1. **Divide:** The input array is divided into two halves, which takes constant time O(1).
2. **Conquer:** Recursively sort both halves of the array. Each recursive call works on half of the array, so the time complexity for this step can be expressed as T(n/2), where n is the size of the input array.
3. **Merge:** Merging the sorted halves into a single sorted array takes linear time O(n), where n is the size of the merged portion.

The recurrence relation for the time complexity of Merge Sort can be expressed as follows:

T(n) = 2T(n/2) + O(n)

Using the Master Theorem or the recurrence tree method, we can determine that the time complexity of Merge Sort is O(n log n) for all cases (best, average, worst). This makes Merge Sort an efficient sorting algorithm for large datasets.

**Space Complexity:**

The space complexity of Merge Sort mainly concerns the additional memory used during the sorting process. Merge Sort requires temporary storage to hold the two halves of the array being merged. The key space usage comes from the recursion stack, as each recursive call consumes memory for function calls and local variables.

1. **Stack Space:** Merge Sort is a recursive algorithm. The maximum depth of the recursion tree is log₂(n), where n is the size of the input array. Therefore, the space complexity due to the recursion stack is O(log n).

2. **Temporary Storage:** During the merging phase, Merge Sort uses temporary storage to hold the two halves of the array being merged. This temporary storage requires O(n) space.

So, the overall space complexity of Merge Sort is O(n) due to the temporary storage, plus O(log n) for the recursion stack. In practical terms, this means that Merge Sort's space complexity is considered linear and is generally more memory-efficient than some other sorting algorithms like Quick Sort, which can have a worst-case space complexity of O(n).

In summary, Merge Sort has a time complexity of O(n log n) and a space complexity of O(n) due to the temporary storage and O(log n) due to the recursion stack. It is a stable and efficient sorting algorithm for a wide range of applications, particularly when space efficiency is important.
'''

def mergeSort(read):
    if len(read) <= 1:
        return read
    mid = len(read) // 2
    left, right = read[:mid], read[mid:]
    left, right = mergeSort(left), mergeSort(right)
    return merge(left, right)

def merge(left, right):
    output = []
    leftIndex, rightIndex = 0, 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            output.append(left[leftIndex])
            leftIndex += 1
        else:
            output.append(right[rightIndex])
            rightIndex += 1
    output.extend(left[leftIndex:])
    output.extend(right[rightIndex:])
    return output

print("Enter the elements: ")
read = list(map(int, input().split()))
print("Elements before sorting...")
print(read)
print("Elements after sorting...")
sortedInput = mergeSort(read)
print(sortedInput)