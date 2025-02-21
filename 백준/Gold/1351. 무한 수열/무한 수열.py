# 첫째 줄에 3개의 정수 n p q
# 첫째 줄에 AN을 출력
# 7 2 3

def func(num):
    if num == 0:
        return 1
    else:
        if num//p not in num_dict:
            num_dict[num//p] = func(num//p)
        
        if num//q not in num_dict:
            num_dict[num//q] = func(num//q)
        return num_dict[num//p] + num_dict[num//q]
        
n,p,q = map(int,input().split())
num_dict = {}

print(func(n))