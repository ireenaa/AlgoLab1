import unittest


def monotonous(arr):
    increasing = True
    decreasing = True
    if len(arr) == 0:
        return False
    if len(arr) < 2:
        return False

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

        if not (increasing or decreasing):
            return False

    return True


array1 = [1, 2, 2, 3]
array2 = [3, 9, 2, 1]
array3 = [1, 1, 3, 1]
array4 = []

print(monotonous(array1))
print(monotonous(array2))
print(monotonous(array3))
print(monotonous(array4))


class TestIsMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(monotonous([1, 2, 3, 4, 5]))
        self.assertTrue(monotonous([1, 1, 1, 1, 1]))
        self.assertTrue(monotonous([1, 2, 2, 4, 4]))
        self.assertTrue(monotonous([-100, 3, 3, 4, 4]))
        self.assertTrue(monotonous([2, 2, 2, 4]))

    def test_decreasing(self):
        self.assertTrue(monotonous([5, 4, 3, 2, 1]))
        self.assertTrue(monotonous([5, 5, 4, 3, 1]))
        self.assertTrue(monotonous([2, 2, 2, -7]))

    def test_not_monotonic(self):
        self.assertFalse(monotonous([1, 2, 1, 4, 5]))
        self.assertFalse(monotonous([]))
        self.assertFalse(monotonous([2]))
        self.assertFalse(monotonous([1,2, 3, 4, 5, -8]))


if __name__ == '__main__':
    unittest.main()
