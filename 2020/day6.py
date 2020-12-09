with open('input6.txt') as f:
    result = 0
    groups = ''.join(f.readlines()).split('\n\n')
    for g in groups:
        answers = g.replace('\n','')
        for a in set(answers):
            if answers.count(a) == len(g.split('\n')):
                result += 1
print(result)
