def counting_sort(arr):
    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Create a counting array to store the count of each element
    count_array = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count_array[num - min_val] += 1

    # Reconstruct the sorted array from the counting array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i + min_val] * count_array[i])

    return sorted_array

# Example usage:
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print("Input Array:", input_array)
print("Sorted Array:", sorted_array)
