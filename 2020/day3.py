i = 0
tree = 0
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        if line[i] is '#':
            tree +=1
        liline=list(line)
        liline[i]='O'
        line = ''.join(liline)
        print(line)
        i+=3
        print(i)
        i = i % len(line)
print(tree)
