# -*- coding:utf-8 -*-
# __author__ = "Kang Sheng"

import numpy as np
import matplotlib.pyplot as plt
from time import clock

from convention import Insert, Bubble, Select
from advanced import BuiltIn, Merge

# set basic information
funcs = [Insert, Bubble, Select, BuiltIn, Merge]
totals = [200, 400, 800, 1600]
plot_method_index = 0

# initial other settings
plot_method = [plt.plot, plt.loglog, plt.semilogx, plt.semilogy][plot_method_index]
times = []
for i in range(len(funcs)):
    times.append([])


def finish(nums):
    """test if an array is sorted corrected."""
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return 'failed!'
    return 'succeeded!'


for total in totals:
    nums = list(np.random.rand(total))  # list is quicker than np.ndarray
    for func_count in range(len(funcs)):
        func = funcs[func_count]
        temp_nums = nums[:]
        start = clock()
        func(temp_nums).sort()
        elapse = clock() - start
        result = finish(temp_nums)
        print('Function %s %s cost %s seconds.' % (func.__name__, result, str(elapse)))
        times[func_count].append(elapse)

for func_count in range(len(funcs)):
    plot_method(totals, times[func_count], label=funcs[func_count].__name__)
    plt.scatter(totals, times[func_count])
plt.legend()
plt.xlabel('total numbers'.title())
plt.ylabel('time consumed (seconds)'.title())
plt.title('sort methods compare'.title())
plt.show()
