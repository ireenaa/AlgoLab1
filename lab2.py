import unittest


def min_time_to_paint(K, T, L):
    left = max(L) * T
    right = sum(L) * T
    while left < right:
        mid = (left + right) // 2
        num_painters = 1
        total_time = 0

        for length in L:
            total_time += length * T
            if total_time > mid:
                num_painters += 1
                total_time = length * T

        if num_painters <= K:
            right = mid
        else:
            left = mid + 1

    print(f"Returning: {left}")
    return left


min_time_to_paint(6, 10, [17, 18, 19, 20, 21])
min_time_to_paint(3, 10, [5, 5, 4, 2, 1])
min_time_to_paint(4, 10, [17, 25, 20, 20, 21])

arr = [30] + [1] * 99
min_time_to_paint(3, 1, arr)
