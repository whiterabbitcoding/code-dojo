What are the steps of binary search?

Steps of the binary search:

    Calculate the middle of the list.
    If the searched value is lower than the value in the middle of the list, set a new right bounder.
    If the searched value is higher than the value in the middle of the list, set a new left bounder.
    If the search value is equal to the value in the middle of the list, return the middle (the index).
    Repeat the steps above until the value is found or the left bounder is equal or higher the right bounder.

What is logarithmic time?

An algorithm is said to have a logarithmic time complexity when it reduces the
size of the input data in each step (it don’t need to look at all values of the
input data), for example:

what is linear time?

Linear Time — O(n)

An algorithm is said to have a linear time complexity when the running time
increases at most linearly with the size of the input data. This is the best
possible time complexity when the algorithm must examine all values in the input
data. For example:

for value in data: print(value)

What is quasilinear time?

Quasilinear Time — O(n log n)

An algorithm is said to have a quasilinear time complexity when each operation
in the input data have a logarithm time complexity. It is commonly seen in
sorting algorithms (e.g. mergesort, timsort, heapsort).

For example: for each value in the data1 (O(n)) use the binary search (O(log n))
to search the same value in data2.

for value in data1: result.append(binary_search(data2, value))
