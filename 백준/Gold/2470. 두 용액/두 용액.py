# 산성 용액과 알칼리성 용액
# 각 용액에는 그 용액의 특성을 나타내는 하나의 정수
# 산성 용액의 특성값은 1부터 10억의 양의 정수
# 알칼리성 용액의 특성값은 -1부터 -10억의 음의 정수
# 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려 한다.
# 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액 찾기

# 전체 용액의 수 N
# 용액의 특성값을 나타내는 N개의 정수

# 두 용액의 특성값을 출력
# 특성값의 오름차순으로 출력
# 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우 그 중 아무것이나 하나를 출력

import sys
INF = sys.maxsize

n = int(input())
array = list(map(int,input().split()))

array.sort()

start = 0
end = len(array) - 1

pair = []
min_val = INF
while start < end:
    total = array[start] + array[end]
    if abs(total) < min_val:
        min_val = abs(total)
        pair = (array[start], array[end])

    if total >= 0:
        end -= 1
    else:
        start += 1

print(*pair)