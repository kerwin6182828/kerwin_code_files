# 用于生成随机数
import numpy as np

def foo(lst):
    if len(lst) <= 1:
        return lst
    count = 0 # 记录该排序流程的计算总次数
    for i in range(len(lst)-1, 0, -1): # 外层循环是不断缩小的，因为后面已经排好序的就不用再比较大小了
        num = 0
        for j in range(i):
            count += 1
            # 逐个比较，前大后小就换位
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                num += 1 # 记录本轮的比较次数
        if num == i: # 当本轮比较次数与i（本轮应比较次数）相等时，意味着已经排好序了
            print("count: ", count)# 返回前打印总计算次数
            return lst
    print("count: ", count)# 返回前打印总计算次数
    return lst

# 1.测试随机顺序所要花费的时间
lst1 = np.random.randint(0, 100, 100)
l1 = foo(lst1)
print("随机数据： ", l1, end="\n\n")

# 2.测试完全逆序所要花费的时间(即为最差时间)
lst2 = np.arange(100, 0, -1)
l2 = foo(lst2)
print("完全逆序 ", l2, end="\n\n")
# 两者的count差异体现在上面的 num==i 就return的代码

# 3.测试完全顺序所要花费的时间(即为最好时间)
lst3 = np.arange(1, 101)
l3 = foo(lst3)
print("完全顺序 ", l3)
