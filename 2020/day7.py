class Bag:
    def __init__(self,color,children):
        self.color = color
        self.children = children
    def __str__(self):
        return self.color+'~'
all_bag = {}
with open('input7.txt') as f:
    rules = f.readlines()
    for r in rules:
        r = r.strip()
        containeur = r.split(' bags contain')[0].strip()
        contained = r.split(' bags contain')[1].split(',')
        if 'no other bag' in contained[0]:
            continue
        child = {}
        for c in contained :
            nb = c.split(' ')[1]
            color = ' '.join(c.split(' ')[2:4]).strip()
            child[color] = nb
        print('-'+containeur+'-')
        all_bag[containeur] = Bag(containeur,child)
result=0
def walk_tree(color,mut):
    global result
    if color in all_bag:
        for new_color,value in all_bag[color].children.items():
            print("-->",mut,color,"is",value,new_color)
            result += int(value)*mut
            print(result)
            walk_tree(new_color,int(value)*mut)

walk_tree('shiny gold',1)

print(result)
