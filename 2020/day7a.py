
visited_color = {'shiny gold':1}
current_color = ['shiny gold']
count = 0
while len(current_color) > 0:
    count +=1
    print('iteration',count)
    new_colors = []
    for color in current_color:
        with open('input7.txt') as f:
            lines = f.readlines()
            for l in lines:
                if ' '+color in l:
                    new_color = ' '.join(l.split(' ')[0:2])
                    if new_color not in visited_color:
                        visited_color[new_color] = 1
                        new_colors.append(new_color)
    current_color = list(set(new_colors))
print(len(visited_color.keys())-1)
