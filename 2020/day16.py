with open('input16.txt') as f:
    lines = f.read().split('\n\n')
    ok = {} # used to quickly filter invalid ticket
    cat = {} # used to guess each index belong to each category
    for l in lines[0].split('\n'):
        ranges = l.split(': ')[1]
        cat_range = {}
        for sub_range in ranges.split(' or '):
            begin = int(sub_range.split('-')[0])
            end = int(sub_range.split('-')[1])
            for i in range(begin,end+1):
                ok[i]=1
                cat_range[i]=1
        cat[l.split(': ')[0]]=cat_range
    success = [] # part B input
    error = 0 # part A result
    for l in lines[2].split('\n')[1:-1]:
        acceptable = True
        for n in l.split(','):
            if int(n) not in ok:
                acceptable = False
                error +=int(n)
                break
        if acceptable:
            success.append(l.split(','))
    print("paf",error)
    fticket = [] # for each ticket we will generate the list of possible value for each field
    for ticket in success:
        ticket_field = []
        for field in ticket:
            possible_field = []
            for name,ranges in cat.items():
                if int(field) in ranges:
                    possible_field.append(name)
            ticket_field.append(possible_field)
        fticket.append(ticket_field)

    attr = {}
    # we will iterate over all the fticket until all field has an index
    while len(attr.keys())<len(cat.keys()): 
        for i in range(len(fticket[0])):
            possible = cat.keys()    
            for f in fticket:
                 possible = [ff for ff in f[i] if ff in possible and not ff in attr]
            if len(possible) == 1:
                attr[possible[0]] = i
        indexes = []
    for name,index in attr.items():
        if "departure" in name: # filter according to puzzle input
            indexes.append(index)
    result = 1 # multiplication so we better use 1 as a starter
    ticket = lines[1].split('\n')[1].split(',')
    for i in indexes:
        result*=int(ticket[i])
    print(result)
