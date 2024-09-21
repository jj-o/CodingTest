# 해설진들은 선수들이 자기 바로 앞 선수를 추월할 때 추월한 선수의 이름을 부른다.
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return

def solution(players, callings):
    player_dict = {player: idx for idx,player in enumerate(players)}
    
    for call in callings:
        idx = player_dict[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        player_dict[players[idx]] = idx
        player_dict[players[idx-1]] = idx-1
    return players