# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수

T = int(input())
dp = [(0,0)]*41
dp[0] = (1,0)
dp[1] = (0,1)

for k in range(2,41):
    dp[k] = (dp[k-1][0]+dp[k-2][0], dp[k-1][1]+dp[k-2][1])

for i in range(T):
    a = int(input())
    print(dp[a][0],dp[a][1])
           
