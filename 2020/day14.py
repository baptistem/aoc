import re
with open('input14.txt') as f:
    lines = f.read().splitlines()
    instru = []
    res = c = {}
    for l in lines:
        var = l.split(' ')[0]
        value = l.split(' ')[-1]
        if 'mask' in var:
            instru.append(c)
            c = {}
            c['mask'] = value
            c['oper'] = {}
        else:
            c['oper'][int(''.join(re.findall('\d+',var)))]=bin(int(value))[2:].zfill(36)
    instru.append(c)
    for ins in instru[1:]:
        for addr,v in ins['oper'].items():
            result = [0] * len(ins['mask'])
            for i,bit in enumerate(list(v)):
                if ins['mask'][i] =='X':
                    result[i]=str(bit)
                elif int(ins['mask'][i]) == 1:
                    result[i] = '1'
                elif int(ins['mask'][i]) == 0:
                    result[i] = '0'
            res[addr]=int(''.join(result),2)
    print('paf',sum(res.values()))
