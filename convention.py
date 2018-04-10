# -*- coding:utf-8 -*-
# __author__ = "Kang Sheng"


class Insert:
    """Insert sort, which is a convention sort method."""

    def __init__(self, nums):
        """Constructor for Insert"""
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        for i in range(1, self.length):
            now = self.nums[i]
            for j in range(i):
                if self.nums[j] > now:
                    k = i
                    while k > j:
                        self.nums[k] = self.nums[k - 1]
                        k -= 1
                    self.nums[j] = now
                    break


class Bubble:
    """Bubble sort, a convention sort method"""

    def __init__(self, nums):
        """Constructor for Bubble"""
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        for i in range(self.length - 1, -1, -1):
            for j in range(i):
                if self.nums[j] > self.nums[j + 1]:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j + 1]
                    self.nums[j + 1] = temp


class Select:
    """Select sort, a convention sort method."""

    def __init__(self, nums):
        """Constructor for Select"""
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        for i in range(self.length - 1, -1, -1):
            max_num = self.nums[i]
            index = i
            for j in range(i + 1):
                if self.nums[j] > max_num:
                    index = j
                    max_num = self.nums[j]
            self.nums[index] = self.nums[i]
            self.nums[i] = max_num
