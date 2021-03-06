# -*- coding:utf-8 -*-
# __author__ = "Kang Sheng"


class BuiltIn:
    """built-in sort method, i.e. sorted()."""

    def __init__(self, nums):
        """Constructor for BuiltInSort"""
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        self.nums.sort()


class Merge:
    """Merge sort, a quick sort method which used recursion method."""

    def __init__(self, nums):
        """Constructor for Merge"""
        self.nums = nums
        self.allay = nums.copy()
        self.length = len(nums)

    def sort(self):
        self.merge_sort(0, self.length)

    def merge_sort(self, start, end):
        if start < end - 1:
            mid = int((end + start) / 2)
            self.merge_sort(start, mid)
            self.merge_sort(mid, end)
            self.merge(start, mid, end)

    def merge(self, start, mid, end):
        """Suppose self.nums[left:mid] and self.nums[mid:end] is sorted correctly."""
        left = start
        right = mid
        index = left
        while left < mid and right < end:
            if self.nums[left] > self.nums[right]:
                self.allay[index] = self.nums[right]
                right += 1
            else:
                self.allay[index] = self.nums[left]
                left += 1
            index += 1
        while left < mid:
            self.allay[index] = self.nums[left]
            left += 1
            index += 1
        while right < end:
            self.allay[index] = self.nums[right]
            right += 1
            index += 1
        for i in range(start, end):
            self.nums[i] = self.allay[i]


class Heap:
    """heapsort, another quick sort method which used recursion and heap method."""

    def __init__(self, nums):
        """Constructor for Heap"""
        self.nums = nums
        self.length = len(nums)
        self.heap_size = len(nums)

    @staticmethod
    def parent(i):
        return int((i - 1) / 2)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def max_heapify(self, i):
        largest = i + 1
        flag = 1
        while largest != i:
            if flag:
                flag = 0
                largest = i
            else:
                i = largest
            left = self.left(largest)
            r = self.right(largest)
            if left < self.heap_size and self.nums[left] > self.nums[i]:
                largest = left
            if r < self.heap_size and self.nums[r] > self.nums[largest]:
                largest = r
            if largest != i:
                temp = self.nums[i]
                self.nums[i] = self.nums[largest]
                self.nums[largest] = temp

    def build_max_heap(self):
        for i in range(int(self.length / 2), -1, -1):
            self.max_heapify(i)

    def sort(self):
        self.build_max_heap()
        for i in range(self.length - 1, 0, -1):
            temp = self.nums[0]
            self.nums[0] = self.nums[i]
            self.nums[i] = temp
            self.heap_size -= 1
            self.max_heapify(0)
        pass


class Quick:
    """Quick sort, a very famous sort method. (Although many sort methods are called 'quick sort'."""

    def __init__(self, nums):
        """Constructor for Quick"""
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        self.quick_sort(0, self.length)
        pass

    def quick_sort(self, start, end):
        if start + 1 < end:
            mid = self.partition(start, end)
            self.quick_sort(start, mid)
            self.quick_sort(mid + 1, end)

    def partition(self, start, end):
        """return a half sorted array which all the left elements is smaller than self.nums[end-1]."""
        mid = self.nums[end - 1]
        left = start
        right = end - 2
        while left < right:
            if self.nums[left] > mid:
                temp = self.nums[left]
                self.nums[left] = self.nums[right]
                self.nums[right] = temp
                right -= 1
            else:
                left += 1
        if mid > self.nums[right]:
            right += 1
        self.nums[end - 1] = self.nums[right]
        self.nums[right] = mid
        return right
