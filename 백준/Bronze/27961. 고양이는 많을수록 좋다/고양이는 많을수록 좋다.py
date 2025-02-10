# 최소의 행동 횟수로 정확히 N마리의 고양이가 되도록 만듦.
# 고양이 1마리 생성
# 고양이 일부 또는 전부를 생성
# 아하 일부 생성도 되네

n = int(input())

if n == 0:
    print(0)
else:
    cnt = 1
    cat = 1

    while cat<n:
        cat = cat*2
        cnt += 1

    print(cnt)
