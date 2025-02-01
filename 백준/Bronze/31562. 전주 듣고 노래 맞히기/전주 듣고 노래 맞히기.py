# 전주를 듣고 먼저 제목을 맞히는 사람이 점수를 얻어 점수가 더 많은 사람이 이김
# 정환은 음을 아는 노래가 N개
# 저장된 노래 중 입력한 첫 세 음으로 시작하는 노래가 여러 개 있어 무슨 노래인지 알 수 없으면 ?
# 첫 세 음만으로 본인이 음을 아는 노래를 맞히는 프로그램

# 정환이 음을 아는 노래의 개수 N
# 정환이 맞히기를 시도할 노래의 개수 M
# 세 음의 음이름이 공백으로 구분하여 주어짐

# 음이름은 각각 C D E F G A B

n,m = map(int,input().split())
song = {}

for _ in range(n):
    t,s,a1,a2,a3,a4,a5,a6,a7 = input().split()
    A = [a1,a2,a3]
    song[s]=A

for _ in range(m):
    B = input().split()
    count = 0
    title = ''

    for s in song:
        if B == song[s]:
            count += 1
            title = s
    
    if count >= 2:
        print('?')
    elif count == 1:
        print(title)
    else:
        print('!')