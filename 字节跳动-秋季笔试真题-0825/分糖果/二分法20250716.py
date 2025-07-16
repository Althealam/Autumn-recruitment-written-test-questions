# 本题和最后一块石头的重量差不多
# 目标：最小化kx-y，其中y为sum(nums)-x
# 因此最小化的目标是：abs(kx-sum(nums)+x) = abs((k+1)x-sum(nums))，并且k为固定值，sum(nums)也是固定值，那么我们需要最小化x即可
# 我们应当尽可能的让(k+1)x-sum(nums)==0，这样才能让kx和y的值尽可能的小，也就是说让x尽可能的去接近sum(nums)//(k+1)


# 思路：找到最小的两个数和最大的两个数，比较这两组数的结果即可

n, k = map(int, input().split()) # n是糖果的堆数，k是计算的系数
nums = list(map(int, input().split())) # 每堆糖果的数量


def solution(nums, n, k):
    if len(nums)<=3: # 如果数组长度小于等于3则直接暴力解法
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = min(res, abs((k+1)*(nums[i]+nums[j])-sum(nums)))
        return res

    nums.sort()

    # 找到最接近sum(nums)//2*k的两堆和
    min_sum = nums[0]+nums[1]
    max_sum = nums[-1]+nums[-2]

    target_sum = sum(nums)/(k+1) # 目标值

    def find_closest(target_sum):
        """找到最接近target_sum的值"""
        closest = float('inf')
        left, right = 0, n-1
        while left<right:
            current_sum = nums[left]+nums[right]
            if abs(current_sum-target_sum)<abs(closest-target_sum):
                closest = current_sum
            
            if current_sum<target_sum:
                left+=1
            elif current_sum>target_sum:
                right-=1
        return closest # 找到的最接近的和
    
    closest_sum = find_closest(target_sum)

    return abs((k+1)*closest_sum-sum(nums))



res = solution(nums, n, k)
print(res)