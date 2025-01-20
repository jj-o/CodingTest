# 4종류의 과일이 최대 5개
# 본인의 카드 뭉치에서 카드 한 장 공개
# 한 종류 이상의 과일이 5개 

n = int(input())
game = {}

for _ in range(n):
    fruit, num = input().split()
    if fruit in game:
        game[fruit] += int(num)
    else:
        game[fruit] = int(num) 

for number in game.values():
    if number == 5:
        print('YES')
        break
else:
    print('NO')