def view_transform(x,y,a):
    occ = 0
    for i in range(-1,2):
        if x+i<0 or x+i>=len(a):
            continue
        for j in range(-1,2):
            if y+j<0 or y+j>=len(a[0]):
                continue
            if i==0 and j ==0:
                continue
            tj = j
            ti = i
            while x+ti>=0 and y+tj>=0 and x+ti<len(a) and y+tj<len(a[0]): 
                if a[x+ti][y+tj] == 'L':
                    break
                if a[x+ti][y+tj] == '#':
                    occ +=1
                    break
                tj+=-int(j<0)+int(j>0)
                ti+=-int(i<0)+int(i>0)

    if a[x][y].strip() == 'L' and occ == 0:
        return '#'
    if a[x][y].strip() == '#' and occ >= 5:
        return 'L'
    return a[x][y]


with open('input11.txt') as f:
    oldlines = []
    newlines = f.read().splitlines()
    while oldlines != newlines:
        oldlines = newlines 
        result = oldlines.copy()
        for x in range(len(oldlines)):
            slines = list(oldlines[x])
            for y in range(len(result[x])):
                slines[y] = view_transform(x,y,oldlines)
            result[x] = ''.join(slines)
        newlines = result.copy()
    print(list(''.join(newlines)).count('#'))
    
