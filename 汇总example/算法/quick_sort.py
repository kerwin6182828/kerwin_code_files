import numpy as np
import time
import random

def quick_sort(lst):
    t1 = time.time()
    count = 0 # 记录该排序流程的计算总次数
    if len(lst) <= 1:
        return lst

    # 实现快排的递归函数
    def recur_pivot(lst):
        # 递归终止条件
        if len(lst) <2:
            return lst

        nonlocal count # 统计总计算次数，由于count是在外部函数定义，而非全局定义，所以此处用nonlocal

        # pop出中枢值，用于划分两边的序列。（这里的中枢值越随机越好,可以防止完全正序时递归深度为n）
        # pivot_value = lst.pop()

        # 此处做了改进，增加了pivot的随机性（可以明显提高顺序序列的效率）
        #  随机读出一个lst中的值作为pivot，并在lst中把这个值删掉，这样把pivot拎出来，后面的递归才可以正常进入终止条件
        pivot_index = random.choice(range(len(lst)))
        pivot_value = lst[pivot_index]
        del lst[pivot_index]

        low_lst = []
        high_lst = []
        for i in lst:
            count += 1
            if i < pivot_value:
                low_lst.append(i)
            else:
                high_lst.append(i)
        return recur_pivot(low_lst) + [pivot_value] + recur_pivot(high_lst) # 这里貌似还真的要把pivot给单独拎出来！否则（1,1,1,1）的情况就不满足递归终止了

    lst = lst.tolist() # 由于ndarry数组没有pop方法，这里把他先转成list
    ordered_lst = recur_pivot(lst)

    # print("quick_sort:")
    print("count: ", count)# 返回前打印总计算次数
    t2 = time.time()
    print("total time: ", t2-t1)
    return ordered_lst

# tip：
# 1.最差的情况是n**2， 跟冒泡和选排的复杂度一样

if __name__ == "__main__":
    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 100)
    l1 = quick_sort(lst1)
    print("随机数据： ", l1, end="\n\n")

    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(100, 0, -1)
    l2 = quick_sort(lst2)
    print("完全逆序 ", l2, end="\n\n")
    # 两者的count差异体现在上面的 num==i 就return的代码

    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 101)
    l3 = quick_sort(lst3)
    print("完全顺序 ", l3)
