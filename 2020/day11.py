

def transform(x,y,a):
    occ = 0
    for i in range(-1,2):
        if x+i<0 or x+i>=len(a):
            continue
        for j in range(-1,2):
            if y+j<0 or y+j>=len(a[0]):
                continue
            if i==0 and j ==0:
                continue
            if x==0 and y==6:
                print(x,y,i,j,a[x+i][y+j])
            if a[x+i][y+j].strip() == "#":
                    occ += 1
    if a[x][y].strip() == 'L' and occ == 0:
        return '#'
    if a[x][y].strip() == '#' and occ >= 4:
        return 'L'
    return a[x][y]

def view_transform(x,y,a)
    occ = 0
    for i in range(-1,2):
        if x+i<0 or x+i>=len(a):
            continue
        for j in range(-1,2):
            if y+j<0 or y+j>=len(a[0]):
                continue
            if i==0 and j ==0:
                continue
            if x==0 and y==6:
                print(x,y,i,j,a[x+i][y+j])
            while x+i>=0 and y+j>=0 and i<len(a) and j<len(a[0]): 
                if a[x+i][y+i] == '#':
                    occ +=1
                    break
                if i ==0:
                    j+=1*j/j
                if j == 0:
                    i+=1*i/i
                else:
                    i+=1*i/i
                    j+=1*j/j

    if a[x][y].strip() == 'L' and occ == 0:
        return '#'
    if a[x][y].strip() == '#' and occ >= 4:
        return 'L'
    return a[x][y]




def parse(lines):
    result = lines.copy()
    for x in range(len(lines)):
        slines = list(lines[x])
        for y in range(len(result[x])):
            slines[y] = transform(x,y,lines)
        result[x] = ''.join(slines)
    return result

with open('input11.txt') as f:
    lines = parse(f.read().splitlines())
    newlines = parse(lines)
    while lines != newlines:
        for l in lines:
            print(l)
        newlines = lines
        lines = parse(lines)
        print()
    print(list(''.join(lines)).count('#'))

