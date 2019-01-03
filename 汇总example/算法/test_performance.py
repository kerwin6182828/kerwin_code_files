import numpy as np
import time
import random

# 导入自己写好的算法function
from select_sort import select_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from shell_sort import shell_sort


if __name__ == "__main__":
    algo_lst = [bubble_sort, select_sort, merge_sort, quick_sort,shell_sort]

    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 100000)
    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(100000, 0, -1)
    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 100001)
    for algo in algo_lst:
        print("【", algo.__name__, "】")
        print("随机数据： ")
        l1 = algo(lst1)
        print("\n\n完全逆序: ")
        l2 = algo(lst2)
        print("\n\n完全顺序: ")
        l3 = algo(lst3)
        print('-------------------------------------', end="\n\n\n\n")


# 算法小结：
#（一万数据级别）
#
# 1. 冒泡、选排的复杂度都为n**n， 都会计算1亿级别次数。冒泡40-60s， 选排20s。 因为选排不需要频繁移动位置         选排 优于  冒泡
# 2. 归并、快排的复杂度都为nlogn， 但实际次数：快排会比归并多3-5倍，但速度往往还是快排快。
#   虽然快排的递归深度往往比归并深，但可能归并当中的移动也比较多，而快排中是申请了额外的空间。
#   （所以空间复杂度比归并高了logn倍，不知道是不是这样也让快排的速度变快了，空间换时间吗？）
#   归并稳定，而快排不稳定
#   数据量大的时候，快排可能会超出最大递归深度，而归并不会！归并的深度为固定的logn！
#   之前总觉得快排的算法没有归并优秀，但是从执行的结果来看，似乎快排更快一些，即使执行的次数更多。。。。
# 3.希尔排序：性能跟增量序列的选取有很大关系。
#   因为后一层的排序速度，会得益于前一层循环中已经排好序的状态，所以复杂度比较难算。
#   （其实我也解释不清楚，总之实际运行情况是上面5种算法中最好的）———— 相比于归并、快排，希尔只用了循坏，不是递归
#   结果看出：希尔排序的运行count最少(120000)，总运行时间也最少(0.06)。


# 注： 上面的随机数据是0-100的小值的随机数。。。
# 其实算法的选择，跟待排序的数据类型有极其密切的关系！！每种算法可能都有适合它的场景。。。。
