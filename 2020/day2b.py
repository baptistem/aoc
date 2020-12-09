with open('input2.txt') as f:
    for line in f:
        line = line.strip()
        position = line.split(' ')[0]
        position_min = int(position.split('-')[0])-1
        position_max = int(position.split('-')[1])-1
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[-1]
        if (password[position_min] is letter or password[position_max] is letter) and not(password[position_min] is letter and password[position_max] is letter):
            print(line)

