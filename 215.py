class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_heapify(array: list, heap_size: int, i):
    """ indexation from 0 """
    left_i = 2 * i + 1
    right_i = 2 * i + 2

    largest_idx = i
    if left_i < heap_size and array[largest_idx] < array[left_i]:
        largest_idx = left_i
    
    if right_i < heap_size and array[largest_idx] < array[right_i]:
        largest_idx = right_i

    if largest_idx != i:
        array[largest_idx], array[i] = array[i], array[largest_idx]

        max_heapify(array, heap_size, largest_idx)

def build_max_heap(array: list):
    heap_size = len(array)
    
    for i in range(len(array)-1, -1, -1):
        max_heapify(array, heap_size, i)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        build_max_heap(nums)
        for i in range(len(nums)-1, len(nums)-1-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(nums, i, 0)
        return nums[-k]

