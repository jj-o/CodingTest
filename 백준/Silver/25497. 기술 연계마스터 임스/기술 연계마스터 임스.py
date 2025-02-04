# 연계 기술 : 사전 기술과 본 기술 두 개의 개별 기술을 순서대로 사용해야만 정상적으로 사용 가능한 기술
# 하나의 사전 기술은 하나의 본 기술과만 연계하여 사용 가능
# 연계할 사전 기술 없이 본 기술을 사용했을 경우에는 게임의 스크립트가 꼬여서 이후 사용하는 기술들이 정상적으로 발동되지 않는다.
# 사전 기술을 사용한 직후에 본 기술을 사용할 필요는 없으며, 중간에 다른 기술을 사용하여도 연계는 정상적으로 이루어진다

# 순서가 꼬이면 이후 사용하는 기술들이 정상적으로 발동 안 됨.
# 사전 -> 본, 둘 다 발동되어야 하나의 기술이 발동동
# L -> R
# S -> K

# N개의 기술을 사용
# 몇 번 정상적 발동되는지

# from collections import deque

n = int(input())
skills = input()
count = 0
# q = deque()
count_SK = 0
count_LR = 0

for s in skills:
    if s.isdigit():
        count += 1
    elif s == 'S':
        count_SK += 1
    elif s == 'K':
        if count_SK > 0:
            count_SK -= 1
            count += 1
        else:
            break
    elif s == 'L':
        count_LR += 1
    elif s == 'R':
        if count_LR > 0:
            count_LR -= 1
            count += 1
        else:
            break

print(count)