class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def partition(arr, low, high):
            pivot_index = random.randint(low, high)
            swap(arr, pivot_index, high)

            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    swap(arr, i, j)

            swap(arr, i + 1, high)
            return i + 1

        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

        quickSort(nums, 0, len(nums) - 1)
        return nums