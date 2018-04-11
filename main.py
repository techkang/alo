# -*- coding:utf-8 -*-
# __author__ = "Kang Sheng"

import numpy as np
import matplotlib.pyplot as plt
from time import clock

from convention import Insert, Bubble, Select
from advanced import BuiltIn, Merge, Heap, Quick

# set basic information
basic_funcs = [Bubble, Insert, Select]
funcs = basic_funcs + [Heap, Merge, Quick, BuiltIn]
totals = [200, 400, 800, 1600]
totals += [10 ** x for x in range(4, 6)]
plot_method_index = 1
debug_mode = False

# debug mode
if debug_mode:
    np.random.seed(1)
    totals = [10]

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
    nums = list(np.random.random_integers(1, total * 10, total))  # list is quicker than np.ndarray
    print('\nInitial numbers succeed! There are %s numbers in total.' % total)
    for func_count in range(len(funcs)):
        func = funcs[func_count]
        if func in basic_funcs and total>1600:
            print('It will take too long for basic sort method %s.' % func.__name__)
            continue
        temp_nums = nums[:]
        start = clock()
        func(temp_nums).sort()
        elapse = clock() - start
        result = finish(temp_nums)
        print('Function %s %s cost %.7s seconds.' % (func.__name__, result, str(elapse)))
        times[func_count].append(elapse)

for func_count in range(len(funcs)):
    plot_method(totals[:len(times[func_count])], times[func_count], label=funcs[func_count].__name__)
    plt.scatter(totals[:len(times[func_count])], times[func_count])
plt.legend()
plt.xlabel('total numbers'.title())
plt.ylabel('time consumed (seconds)'.title())
plt.title('sort methods compare '.title()+'(plot method: %s)' % plot_method.__name__)
if not debug_mode:
    plt.show()

