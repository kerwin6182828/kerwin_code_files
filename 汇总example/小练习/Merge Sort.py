import numpy as np
import time

def MergeSort(lst):
    def merge(lst, left, mid, right):
        """
        function: 将两个子序列合并
        """
        No1_left = left
        No1_right = mid -1
        No2_left = mid
        No2_right = right
        temp_lst = [] # 用于临时存放合并中的序列

        nonlocal count # 统计总计算次数，由于count是在外部函数定义，而非全局定义，所以此处用nonlocal

        # 不断比较两个序列的最小值，把更小的一个放入temp_lst
        while No1_left<=No1_right and No2_left<=No2_right:
            count += 1
            if lst[No1_left] <= lst[No2_left]:
                temp_lst.append(lst[No1_left])
                No1_left += 1
            else:
                temp_lst.append(lst[No2_left])
                No2_left += 1
        # 上面的while循环结束后，就意味着一个子序列为空了，此时把另一个子序列全部放入temp_lst中即可
        while No1_left<=No1_right:
            count += 1
            temp_lst.append(lst[No1_left])
            No1_left += 1
        while No2_left<=No2_right:
            count += 1
            temp_lst.append(lst[No2_left])
            No2_left += 1

        lst[left:right+1] = temp_lst # 用切片的形式，把temp_lst的值迁移到lst的对应索引位置上



    # 放入的left，right 是对lst的索引值
    def recur_bin(lst, left, right): # eg. left=0, right=2 ----> 则mid为1;  l:0,r:1,则：mid=0
        """
        function:不断递归二分，直到left==right
        """
        if left == right: #  这时候意味着只传进一个索引，已经不能再二分，所以为递归停止的条件
            return
        mid = (left+right)//2
        recur_bin(lst, left, mid)
        recur_bin(lst, mid+1, right) # 这里的mid+1很讨巧，刚好使这两个递归调用都可以满足终止条件
        merge(lst, left, mid+1, right) # 这里的left，mid，right 都是索引，既然要做切分，索引又不能重复所以这里mid要+1


    t1 = time.time()
    if len(lst) <= 1:
        return lst
    count = 0
    left = 0
    right = len(lst)-1
    recur_bin(lst, left, right)
    print("count: ", count)# 返回前打印总计算次数
    t2 = time.time()
    print("total time: ", t2-t1)
    return lst




if __name__ == "__main__":
    # 1.测试随机顺序所要花费的时间
    lst1 = np.random.randint(0, 100, 100)
    l1 = MergeSort(lst1)
    print("随机数据： ", l1, end="\n\n")

    # 2.测试完全逆序所要花费的时间(即为最差时间)
    lst2 = np.arange(100, 0, -1)
    l2 = MergeSort(lst2)
    print("完全逆序 ", l2, end="\n\n")
    # 两者的count差异体现在上面的 num==i 就return的代码

    # 3.测试完全顺序所要花费的时间(即为最好时间)
    lst3 = np.arange(1, 101)
    l3 = MergeSort(lst3)
    print("完全顺序 ", l3)
