# N개의 물건, 최대 C만큼의 무게를 넣을 수 있는 가방
# 둘째 줄에 물건의 무게

# N개의 물건을 가방에 넣는 방법의 수
# 첫째 줄에 가방에 넣는 방법의 수를 출력

from bisect import bisect_right
from itertools import combinations

def get_sub_sums(arr):
    sub_sums = []
    n = len(arr)
    for i in range(n+1):
        # 물건 중 i개를 뽑아 combination 함함
        for comb in combinations(arr,i):
            sub_sums.append(sum(comb))
    return sub_sums

n,c = map(int,input().split())
items = list(map(int,input().split()))

# 배열을 반으로 나눔
left = items[:n//2]
right = items[n//2:]

left_sums = get_sub_sums(left)
right_sums = get_sub_sums(right)

right_sums.sort()

# 가능한 조합의 수 계산산
count = 0
for x in left_sums:
    # 오른쪽에서 c-x 이하인 값의 개수를 섽다.
    # left_sum + right_sum <= c
    count += bisect_right(right_sums, c-x)
    
print(count)