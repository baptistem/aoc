def parse(line):
        element = line.strip().split(' ')
        return (element[0], int(element[1]))

with open('input8.txt') as f:
    lines = f.readlines()
    flines = []
    for l in lines:
        flines.append(parse(l))
    i = 0
    j = 0 # set to 999 for part a
    while i <= len(flines) and j <= len(flines):
        new_lines = flines.copy()
        while j < len(flines):
            act,arg = flines[j]
            if act in 'nopjmp':
                if act =='nop':
                    new_lines[j] = ('jmp',arg)
                else:
                    new_lines[j] = ('nop',arg)
                break
            j +=1
        j+=1
        i = 0
        acc = 0
        visited_i = {}
        fail = False
        while i < len(new_lines):
            action,arg = new_lines[i]
            if i in visited_i:
                print('fail, looping with an acc of',acc)
                fail = True
                break
            else:
                visited_i[i]=(action,arg)
            if action == 'nop':
                i += 1
                continue
            if action == 'acc':
                i += 1
                acc += int(arg)
                continue
            if action == 'jmp':
                i += int(arg)
        if not fail:
            print(i)
            print('tadaaa',acc)
            break
    if j > len(flines):
        print('failure')
