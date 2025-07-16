n, k = map(int, input().split()) # n是糖果的堆数，k是计算的系数
nums = list(map(int, input().split())) # 每堆糖果的数量

min_result = float('inf')
for i in range(n):
    for j in range(i+1, n):
        x = nums[i]+nums[j]
        current = abs((k+1)*x - sum(nums))
        if current<min_result:
            min_result = current
print(min_result)