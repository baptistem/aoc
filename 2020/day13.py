
with open('input13.txt') as f:
    lines = f.read().splitlines()
    t = int(lines[0])
    best_bus_id = 0
    best_bus_time = 9999
    for b in lines[1].split(','):
        if b == 'x':
            continue
        ib = int(b)
        cb = ib * int(t/ib)
        ncb = cb+ib
        if ncb-t < best_bus_time:
            best_bus_time = ncb-t
            best_bus_id = ib
    print(best_bus_id*best_bus_time)
