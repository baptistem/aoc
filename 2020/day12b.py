
with open('input12.txt') as f:
    lines = f.read().splitlines()
    d = {
            'N':90,
            'E':180,
            'S':270,
            'W':0
    }

    dxy = {
            90:(0,1,'N'),
            180:(1,0,'E'),
            270:(0,-1,'S'),
            0:(-1,0,'W')
    }
    wx = 10
    wy = 1
    x = 0
    y = 0
    for l in lines:
        print()
        print(l,f"boat {x},{y} wp {wx},{wy}")
        if l[0] == 'F':
            x += wx*int(l[1:])
            y += wy*int(l[1:])
        if l[0] in d:
            mv = dxy[d[l[0]]]
            wx += mv[0]*int(l[1:])
            wy += mv[1]*int(l[1:])
        if l[0] in 'RL':
            o = l[0]
            deg = int(l[1:])
            if (o == 'R' and deg == 90) or (o == 'L' and deg == 270):
                wx,wy = wy,-wx
            if deg == 180:
                wx ,wy = -wx, -wy
            if (o =='R' and deg == 270) or (o =='L' and deg == 90):
               wx, wy =-wy, wx
        print(l,f"boat {x},{y} wp {wx},{wy}")
    print(abs(x)+abs(y))
