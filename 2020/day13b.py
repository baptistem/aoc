from sympy.ntheory.modular import crt
with open('input13.txt') as f:
    lines = f.read().splitlines()
    bus_mod = []
    bus_line = []
    for i,b in enumerate(lines[1].split(',')):
        if b == 'x':
            continue
        ib = int(b)
        bus_mod.append(-i)
        bus_line.append(ib)
    print(crt(bus_line,bus_mod)[0])

