with open('input2.txt') as f:
    for line in f:
        line = line.strip()
        nb = line.split(' ')[0]
        nb_min = int(nb.split('-')[0])
        nb_max = int(nb.split('-')[1])
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[-1]
        if nb_min <= len(password.split(letter))-1 <= nb_max:
            print(line)

