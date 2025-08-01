# 思路：求出每个1之间的差值即可
n = int(input())
stones = list(map(int, input().split()))

stones.append(1) # 在右侧增加一个石头
ans = 0 
last = -1 # 上一个有石头的索引
for i in range(len(stones)):
    if stones[i]==1: # 当前走到的路是石头
        ans = max(ans, i-last)
        last = i
print(ans)
