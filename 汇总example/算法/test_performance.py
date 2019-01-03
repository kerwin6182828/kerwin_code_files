import numpy as np
import time
import random

# 导入自己写好的算法function
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from select_sort import select_sort
from shell_sort import shell_sort


if __name__ == "__main__":
    algo_lst = [bubble_sort, select_sort, merge_sort, quick_sort,shell_sort]

    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 10000)
    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(10000, 0, -1)
    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 10001)
    for algo in algo_lst:
        print("【", algo.__name__, "】")
        print("随机数据： ")
        l1 = algo(lst1)
        print("\n\n完全逆序: ")
        l2 = algo(lst2)
        print("\n\n完全顺序: ")
        l3 = algo(lst3)
        print('-------------------------------------', end="\n\n\n\n")
