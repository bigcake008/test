def find_smallest(target_array):
    smallest = target_array[0]
    smallest_index = 0
    for i in range(1, len(target_array)):
        if smallest > target_array[i]:
            smallest = target_array[i]
            smallest_index = i
    return smallest_index


def selection_sort(target_array):
    new_array = []
    array_len = len(target_array)
    for i in range(array_len):
        smallest = find_smallest(target_array)
        new_array.append(target_array.pop(smallest))
    return new_array


print(selection_sort([5, 3, 6, 2, 10]))
