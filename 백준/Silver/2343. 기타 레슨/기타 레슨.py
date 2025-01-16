# 총 N개의 강의
# i번 강의와 j번 강의 i와 j 사이의 모든 강의도 같은 블루레이에 녹화

# M개의 블루레이에 모든 기타 강의 동영상 녹화
# 블루레이의 크기를 최소
# M개의 블루레이 모두 같은 크기

# 강의의 길이가 분 단위
# 가능한 블루레이의 크기 중 최소를 구하는 프로그램

# 강의의 수 n,m 이 주어짐
# 강토의 기타 강의의 길이가 강의 순서대로 자연수 주어진다. 
# 강의의 길이는 10000분 넘지 않는다.

# 가능한 블루레이 크기 중 최소 출력
# 블루레이의 크기의 최소

# 9 3
# 1 2 3 4 5 6 7 8 9

n,m = map(int,input().split())
time = list(map(int,input().split()))
start = max(time)
end = sum(time)

while start <= end:
    mid = (start + end)//2
    total = 0
    count = 1
    for t in time:
        if total + t > mid:
            count += 1
            total = 0
        total += t

    if count <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid +1

print(ans)