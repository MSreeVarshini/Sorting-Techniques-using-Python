# Selection Sort
'''Here's a detailed complexity analysis of Selection Sort in Python, including its best-case and worst-case scenarios:

1. Time Complexity:

- Worst-case time complexity: O(n^2)
  - This occurs when the input array is in reverse order, and for each element, we have to compare it with all the remaining elements to find the minimum and swap it.

- Best-case time complexity: O(n^2)
  - This occurs when the input array is already sorted, but Selection Sort still needs to make comparisons for each element to verify that it is the smallest. Although no swaps are needed in the best case, the algorithm still performs a quadratic number of comparisons.

- Average-case time complexity: O(n^2)
  - On average, Selection Sort makes roughly n/2 + n/3 + n/4 + ... + 1 comparisons, which is still O(n^2) due to the quadratic nature of the algorithm.

2. Space Complexity:
- Selection Sort is an in-place sorting algorithm, meaning it doesn't require additional memory to sort the array. Its space complexity is O(1), indicating that it uses a constant amount of extra memory for temporary variables and swaps.

 *Best-case scenario: The best-case scenario occurs when the input array is already sorted. In this case, Selection Sort performs a quadratic number of comparisons but doesn't require any swaps. Despite not having to perform swaps, the best-case time complexity remains O(n^2) because the algorithm still compares each element with all other elements.

 *Worst-case scenario: The worst-case scenario occurs when the input array is in reverse order or nearly reverse order. In this case, Selection Sort will perform the maximum number of comparisons and swaps for each element. The worst-case time complexity is O(n^2), as for each element, it will need to compare it with all the remaining elements, leading to a quadratic number of comparisons and swaps.

In summary, Selection Sort's best-case and worst-case time complexities are both O(n^2), which makes it inefficient for large datasets or lists compared to more efficient sorting algorithms with better average-case and worst-case time complexities, such as Quick Sort or Merge Sort (O(n log n)).
'''


def selectionSort(read):
    for i in range(len(read)):
        min_index = i
        for j in range(i+1, len(read)):
            if read[min_index]>read[j]:
                min_index = j
        read[i], read[min_index] = read[min_index], read[i]

print("Enter the elements: ")
read = list(map(int, input().split()))
print("Elements before sorting...")
print(read)
print("Elements after sorting...")
selectionSort(read)
print(read)