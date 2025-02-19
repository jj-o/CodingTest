# LCS(최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것
# ACAYKP CAPCAK
# 입력으로  주어진 두 문자열의 LCS의 길이
# 한 문자열에서 k번째 index에서 부분 수열의 길이

sentence1 = input()
sentence2 = input()

dp = [[0] * (len(sentence2)+1) for _ in range(len(sentence1)+1)]


# 인덱스가 i일 때, j는 계속 변화하니까 같은 숫자 아님님
for i in range(1,len(sentence1)+1):
    for j in range(1,len(sentence2)+1):
        if sentence1[i-1] == sentence2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# print(dp)
print(dp[len(sentence1)][len(sentence2)])
            