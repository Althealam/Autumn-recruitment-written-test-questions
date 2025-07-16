# 思路：对于每个点[i, j]，求解其j/i的斜率值，然后判断后面的点的斜率值是否相同，如果相同的话那么这两个节点是一对符合条件的节点对

n = int(input()) # 点的数量
nums = list(map(int, input().split()))
points = []
ind = 1 # 初始的下标值
for num in nums:
    points.append([ind, num])
    ind+=1

from collections import defaultdict
xielv = defaultdict(int) # 计算不同的斜率值的点对数量
for x, y in points:
    gd = y/x
    if gd not in xielv.keys():
        xielv[gd]=1
    else:
        xielv[gd]+=1


def zuheshu(n):
    """计算A(n, 2)的组合数"""
    ans = n*(n-1)//2
    return ans
    
res = 0
for k, v in xielv.items(): # 计算组合数
    if v>1: # 该斜率相同的节点数大于1
        x = zuheshu(v)
        res+=x
print(res)

         
