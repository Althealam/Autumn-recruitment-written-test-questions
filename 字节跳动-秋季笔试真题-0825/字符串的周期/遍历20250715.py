# 思路
# 1. 枚举可能的周期k，k的取值范围为1<=k<=n
# 2. 检查k是否为有效周期
# （1）s[i]和s[i+k]都是0或者1，必须相等
# （2）s[i]和s[i+k]其中一个是*
# （3）如果s[i]和s[i+k]为不同的非*字符，那么k无效
# 3. 确定周期的具体形式
# （1）遍历周期内的每个位置，收集该位置在整个字符串中所有对应位置的非*字符
# （2）如果所有对应位置的非*字符相同，则该位置确定为该字符，否则保留为*

# 注意：字符串可以由长度为k的子串重复拼接而成，最后一段可能不完整，但是必须匹配前面k个字符
s = input().strip()

def is_valid(k, s):
    n = len(s)
    # 遍历周期内的每个位置（0到k-1）
    for pos_in_period in range(k):
        # 收集该位置在所有周期片段中的非*字符
        chars = set()
        # 遍历所有包含该位置的片段（pos_in_period, pos_in_period+k, pos_in_period+2k...）
        for j in range(pos_in_period, n, k):
            c = s[j]
            if c != '*':  # 只关注非*字符
                chars.add(c)
        # 如果同一位置出现两种不同的非*字符，说明无法通过替换*使它们一致，周期无效
        if len(chars) > 1:
            return False
    return True


# 寻找合适的周期值
min_k = float('inf')
for k in range(1, len(s)+1): # 遍历可能的周期值
    # print(f"正在检查周期值{k}")
    remainder = len(s) % k
    padding = 0 if remainder == 0 else (k-len(s)+(len(s)%k)*k)
    new_s = s + '*' * padding
    # print(new_s)
    if is_valid(k, new_s):
        # print(f"{k}是合法的周期值")
        min_k = min(min_k, k)
        break


# 寻找合适的周期
def find_period(min_k, s):
    if min_k == len(s):
        print(min_k)
        print(s)
    else:
        base_char = s[:min_k]
        period = list(base_char)
        for j in range(0, len(s), min_k):
            if j+min_k<len(s): # 最小周期值在len(s)的范围内
                cur_char = s[j:j+min_k] # 第j段字符串
            else: # 最小周期值超过了len(s)的范围
                cur_char = s[j:]+'*'*(min_k-len(s)+j)
            # print("当前的字符串为:", cur_char)
            for i in range(min_k):
                if period[i]!=cur_char[i] and period[i]=='*':
                    period[i]=cur_char[i]
                # print(f"当前的period[{i}]为:", period[i])
        print(min_k)
        print(''.join(period))

find_period(min_k, new_s)
