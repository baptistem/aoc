import re

count = 0
required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
reg = {
        'byr': lambda e : 1920 <= int(e) <= 2002,
        'iyr': lambda e : 2010 <= int(e) <= 2020,
        'eyr': lambda e : 2020 <= int(e) <= 2030,
        'hgt': lambda e : ('cm' in e and 150 <= int(e.split('cm')[0]) <= 193) or ('in' in e and 59 <= int(e.split('in')[0]) <= 76),
        'hcl': lambda e : re.match('#[0-9a-f]{6}',e),
        'ecl': lambda e : e in ['amb','blu','brn','gry','grn','hzl','oth'],
        'pid': lambda e : re.match('[0-9]{9}',e)
        }
def validate(p):
    keyvalue = p.split(' ')
    key = {}
    for k in keyvalue:
        if ':' in k :
          key[k.split(':')[0]]=k.split(':')[1]
    kk = ''.join(list(key.keys()))
    ok = 0
    for r in required:
        if r not in key:
            return 0
        if reg[r](key[r]):
            ok += 1
        else:
            return 0
    if ok == len(required):
      return 1
    else:
      return 0
with open('input4.txt') as f:
    lines = ''.join(f.readlines())
    passports = lines.split('\n\n')
    for p in passports:
        cleanp = p.replace('\n',' ')
        count += validate(cleanp)
print(count)
