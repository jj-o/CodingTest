def solution(park, routes):
    x,y = 0,0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x,y=j,i
                break
                
    for route in routes:
        xx,yy = x,y
        for step in range(int(route[2])):
            if route[0] == 'E' and xx!= len(park[0])-1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2])-1:
                    x = xx
            elif route[0] == 'W' and xx!=0 and park[yy][xx-1] != 'X':
                xx -=1
                if step == int(route[2])-1:
                    x = xx
            elif route[0] == 'S' and yy!=len(park[0])-1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2])-1:
                    y = yy
            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(route[2])-1:
                    y = yy
    return [y,x]