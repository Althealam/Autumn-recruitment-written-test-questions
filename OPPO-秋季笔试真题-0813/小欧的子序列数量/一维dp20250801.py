# 注意本题中11必须要是连续的
# 1. dp数组以及下标的含义：dp[i][0/1/2]表示前面i个数字中包含的11, 114, 1145串的数量
# 2. 递推公式：
# (1) s[i]==1 and s[i-1]==1: dp[i][0]=dp[i-1][0]+1
# (2) s[i]==4: dp[i][1]=dp[i-1][0]+dp[i-1][1]+1 
# (3) s[3]==5: dp[i][2]=dp[i-1][2]+dp[i-1][1]+1 


n = int(input())
nums = str(input())
MOD = 10000000007

dp = [0]*3
for i in range(n):
    if nums[i]=='1' and nums[i-1]=='1': # 需要保证11为连续字符
        dp[0]+=1
    elif nums[i]=='4': # 找114的数量：前面i-1个字符的114的数量+前面i-1个字符的11的数量
        dp[1]+=dp[0]
    elif nums[i]=='5': # 找1145的数量：前面i-1个字符的1145的数量+前面i-1个字符的114的数量
        dp[2]+=dp[1]


print(dp[2]%MOD)
        
