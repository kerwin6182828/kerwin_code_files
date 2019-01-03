import numpy as np
import time

def select_sort(lst):
    t1 = time.time()
    count = 0 # 记录该排序流程的计算总次数
    if len(lst) <= 1:
        return lst

    lenth = range(len(lst)) # 列表长度
    for i in lenth:# 最外层的循环一定是要整个lenth（即：lst中的每一个元素都要选中一次）
        min_index = i # 假设我选中的元素就是最小值，那么i就是最小值的索引
        for j in range(i+1, len(lst)): # 前面的i是之前几轮循环中挑出来的最小值，这里不需要考虑他们，所以从i+1开始
            count += 1
            if lst[j] < lst[min_index]: # 逐个比较，当有比min_index索引上的值还小的数，则把那个数的索引作为最小索引
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i] #  外层循环的一轮结束后，进行换位置

    # print("select_sort:")
    print("count: ", count)# 返回前打印总计算次数
    t2 = time.time()
    print("total time: ", t2-t1)
    return lst

# tip：
# 1.可能是比冒泡还要简单的算法（也是最符合人类行为的一种）而且实际速度比冒泡要快

if __name__ == "__main__":
    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 100)
    l1 = select_sort(lst1)
    print("随机数据： ", l1, end="\n\n")

    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(100, 0, -1)
    l2 = select_sort(lst2)
    print("完全逆序 ", l2, end="\n\n")
    # 两者的count差异体现在上面的 num==i 就return的代码

    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 101)
    l3 = select_sort(lst3)
    print("完全顺序 ", l3)
