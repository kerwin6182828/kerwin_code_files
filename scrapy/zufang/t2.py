def BubbleSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    count = 1
    for i in range (0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
            print("count: ", count)
            count += 1
    return lst
x=input("请输入待排序数列：\n")
# y=x.split()
y = list(x)
arr=[]
for i in  y:
    print(i)
    arr.append(int(i))
arr=BubbleSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
