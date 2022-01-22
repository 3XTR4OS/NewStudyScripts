spisok = list(range(256))


def binary_seach(list, item):
    low = 0
    high = len(spisok) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]

        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return 'item not in list'

# print(binary_seach(spisok, 162))
