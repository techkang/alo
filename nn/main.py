# -*- coding:utf-8 -*-
# __author__ = "Kang Sheng"

import numpy as np
import matplotlib.pyplot as plt
import time


def distance(a, b):
    """Calculate Euclid distance between point a and point b."""
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def brutal(points, start, end):
    min_distance = max_distance
    for i in range(start, end):
        for j in range(start, i):
            if min_distance > distance(points[i], points[j]):
                min_distance = distance(points[i], points[j])
    return min_distance


def nn(points, start, end):
    if end - start < 2:
        # print('Some thing error!!!')
        return max_distance
    elif end - start == 2:
        return distance(points[start], points[start + 1])
    elif end - start < 4:
        return brutal(points, start, end)
    else:
        mid = int((end + start) / 2)
        nn_l = nn(points, start, mid)
        nn_r = nn(points, mid, end)
        d = min(nn_l, nn_r)
        left = start
        right = end - 1
        for i in range(start, mid + 1):
            if points[i][0] > points[mid][0] - d:
                left = i
                break
        for i in range(end - 1, mid - 1, -1):
            if points[i][0] <= points[mid][0] + d:
                right = i
                break
        nn_m = nn(points, left, right)
        return min(nn_m, d)


if __name__ == '__main__':

    # settings
    totals = [10, 20, 40, 80]
    debug_mode = False

    # other settings
    max_distance = 200
    if debug_mode:
        np.random.seed(4)
    else:
        totals+=[2**x*160 for x in range(6)]

    times = []

    plt.ion()

    for total in totals:
        # initial points
        points_x = np.random.rand(total) * 100
        points_y = np.random.rand(total) * 100
        points = [x for x in zip(points_x, points_y)]
        points.sort()
        start = time.clock()
        min_distance = nn(points, 0, total)
        elapse = time.clock() - start
        print('Total numbers: %s, time elapsed: %.7s' % (total, elapse))
        times.append(elapse)

        if debug_mode:
            min_debug = distance(points[0], points[1])
            for i in range(total):
                for j in range(i):
                    if min_debug > distance(points[i], points[j]):
                        min_debug = distance(points[i], points[j])
            # print('min distance(by brutal method): ', min_debug)
            if not min_distance == min_debug:
                print('Error!')
        plt.cla()
        plt.scatter(points_x, points_y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Total numbers: %s' % total)
        plt.pause(1)
    plt.title('Total numbers: %s. Finished!' % total)
    plt.ioff()
    if not debug_mode:
        plt.show()
    plt.plot(totals,times)
    plt.scatter(totals,times)
    plt.xlabel('total numbers'.title())
    plt.ylabel('Time consumed (seconds)')
    plt.title('nearest neighboor')
    plt.show()
