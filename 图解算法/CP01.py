def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1
    while low < high:
        mid = (high + low) // 2
        guess = input_list[mid]
        # print(guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            print('high', high)
        else:
            low = mid + 1
            print('low', low)
    return None


test_list = [1, 3, 5, 7, 9, 11]
print('target', binary_search(test_list, 11))
print(1 // 2)

