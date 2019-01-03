import numpy as np
import time

def shell_sort(lst):
    t1 = time.time()
    count = 0 # 记录该排序流程的计算总次数
    if len(lst) <= 1:
        return lst

    #  增量的选择是希尔排序的关键（eg。如果长度为10，增量序列为5，2,1）
    inc = len(lst) // 2 # 增量序列的初始值（我只是没有把增量的值放入list中，道理是一样，都会有个增量序列）
    while inc >= 1:# 当增量大于等于1时
        for i in range(inc, len(lst)):# 若增量为2，则从2取到9 (不用取第一波数)
            while (i >= inc and lst[i] < lst[i-inc]):# 即：不断把后面的数与前一个“增量元素”去比,当索引取值在第一波数时，退出循环，取取下一个数
            # 因为前面已经排好序了，那此时取到的数若比前一个大，则比前面都大
                count += 1
                lst[i], lst[i-inc] = lst[i-inc], lst[i] # 如果此时的索引取值小于前一个“增量元素”，则换位，并继续往前一个”增量元素”比较
                i -= inc
            else:
                count += 1
        inc = inc // 2 # 使用下一个增量

    # print("shell_sort:")
    print("count: ", count)# 返回前打印总计算次数
    t2 = time.time()
    print("total time: ", t2-t1)
    return lst

# tip：
# 1.由于增量序列的存在，可以实现长距离的移位来提高效率。
# 2.大增量下排好序的情况下，对下一个增量的排序有一定促进作用，所以复杂度并容易计算

if __name__ == "__main__":
    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 100)
    l1 = shell_sort(lst1)
    print("随机数据： ", l1, end="\n\n")

    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(100, 0, -1)
    l2 = shell_sort(lst2)
    print("完全逆序 ", l2, end="\n\n")
    # 两者的count差异体现在上面的 num==i 就return的代码

    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 101)
    l3 = shell_sort(lst3)
    print("完全顺序 ", l3)
