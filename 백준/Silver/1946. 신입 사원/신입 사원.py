# 서류심사와 면접 시험
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는자만 선발
# 진영 주식회사가 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수
# 선발할 수 있는 신입사원의 최대인원수
# 숫자는 순위위

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    point = []
    n = int(input())
    for i in range(n):
        p,m = map(int,input().split())
        point.append((p,m))
    point.sort(key=lambda x:x[0])
    count = 1
    check = point[0][1]
    for i in range(1,n):
        if check > point[i][1]:
            check = point[i][1] # 이제 check 기준이 이것으로 변함함
            count += 1
    print(count)