
def get_new(last,i,mem_i):
    if last not in mem_i:
        result = 0
    elif mem_i[last] == i-1:
        result = 1
    else:
        result = i -1 - mem_i[last]
    #print(f"turn {i}, last is {last}, new is {result}")
    return result



mem = [2,1,10,11,0,6]
mem_i = {}
for i,m in enumerate(mem) :
    mem_i[m]=i+1
last = 0

for i in range(len(mem)+2,30000000+1):
    new = get_new(last,i,mem_i)
    mem_i[last] = i-1
    last = new
print(last)

