# 가장 긴 증가하는 부분 수열
# 수열 A의 크기
# 수열 A를 이루고 있는 Ai
# 수열 A의 가장 긴 증가하는 부분 수열의 길이

# 왜 다이나믹 프로그래밍이지?
# -> 최장 증가 부분 수열의 길이를 dp로 한다.
# -> i에서 끝나는 증가 부분 수열

N = int(input())
numbers = list(map(int,input().split()))
dp = [1] * 1000

# 그런데 2번째 인덱스에서 시작하는 것이 더 나을수도 있는데?
# 이중 for문으로 해결
# dp에 들어가는 것은 수열의 길이

for i in range(1,N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))
