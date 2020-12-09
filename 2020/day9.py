
def is_possible(nb,prev):
    # check if the number is the sum of an element in list
    # by doing the minus we avoid computing the whole matrice, and I am lazy to do it anyway
    for e in prev:
        if nb-e in prev:
            return True
    return False

def get_sum(nb,prev):
    buf = []
    for i in prev:
        buf.append(i)
        # we check if the buffer is not too big and reduce it if so
        while sum(buf) > nb:
            buf = buf[1:]

        # here is part B victory
        if sum(buf) == nb:
            buf.sort()
            print('tadaaa',buf[0]+buf[-1])
            break

with open('input9.txt') as f:
    lines = f.read().splitlines()
    # I don't want to bother with strings, I want integer
    ilines = [ int(e) for e in lines]
    # loop starting from the 25 elements
    for i,nb in enumerate(ilines[25:],start=25):
        if not is_possible(nb,ilines[i-25:i]):
            # this is part A victory
            print('paf',nb)
            get_sum(nb,ilines[:i])
            break
        i+=1
