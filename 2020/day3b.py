i = 0
tree = 0
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        if line[i] == '#':
            tree +=1
            inter = ' --> '
        else:
            inter = '     '
        liline=list(line)
        liline[i]='O'
        linec = ''.join(liline)
        i+=1
        i = i % len(line)
tree1 = tree
i = 0
tree = 0
print(tree1)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        if line[i] == '#':
            tree +=1
        liline=list(line)
        liline[i]='O'
        line = ''.join(liline)
        i+=3
        i = i % len(line)
tree2 = tree
tree = 0
i = 0
print(tree2)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        if line[i] == '#':
            tree +=1
        liline=list(line)
        liline[i]='O'
        line = ''.join(liline)
        i+=5
        i = i % len(line)
tree3 = tree
i = 0
tree = 0
print(tree3)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        if line[i] == '#':
            tree +=1
            inter = ' --> '
        else:
            inter = '     '
        liline=list(line)
        liline[i]='O'
        linec = ''.join(liline)
        print(line+inter+linec)
        i+=7
        i = i % len(line)
tree4 = tree
i = 0
tree = 0
print(tree4)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
with open('input3.txt') as f:
    lines = f.readlines()
    linei = iter(lines)
    try:
      while True:
        line = next(linei).strip()
        if line[i] == '#':
            tree +=1
            inter = ' --> '
        else:
            inter = '     '
        liline=list(line)
        liline[i]='O'
        linec = ''.join(liline)
        i+=1
        i = i % len(line)
        print(line+inter+linec)
        line=next(linei).strip()
        print(line+'     '+line)
    except (StopIteration):
        pass
tree5 = tree
print(tree1)
print(tree2)
print(tree3)
print(tree4)
print(tree5)
print(tree1*tree2*tree3*tree4*tree5)
