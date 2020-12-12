
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
    cd = d['E']
    x = 0
    y = 0
    for l in lines:
        mv = (0,0,dxy[cd][2])
        if l[0] == 'F':
            mv = dxy[cd]
        if l[0] in d:
            mv = dxy[d[l[0]]]
        print(f"ship is going {dxy[cd][2]}, current position is {x},{y}, movement is {mv}, line is {l}")
        x += mv[0]*int(l[1:])
        y += mv[1]*int(l[1:])

        mult = int(l[1:])*int(l[0]=='R') - int(l[1:]) * int(l[0]=='L')
        cd = (cd + mult) % 360
        print(mult,cd)
    print(abs(x)+abs(y))
