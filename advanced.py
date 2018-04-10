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
    """Merge sort, a qucik sort method which used recursion method."""

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
