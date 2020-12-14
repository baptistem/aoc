import re

def xbin2lbin(chain):
    result = []
    # we count the number of X
    nbx = chain.count('X')
    # we save where theses X are
    x_indexes= [ i for i,x in enumerate(chain) if x=='X']
    # so we want to get all the permutation possible
    # instead of replacing string over and over which is too costy we cheat
    # the idea is to get permutation of 1 and 0 in a string of nbx length
    # which is basicly counting from 0 to 2**nbx
    # so if there is 4 X, we will go from 0000 to 1111
    # but wait, 1111 is 15 not 16? thanks to range() it ends before 2**nbx
    for i in range(2**nbx):
        bi = bin2str(i,nbx)
        # bi is possible value
        res = list(chain)
        for bi_index,x_index in enumerate(x_indexes):
            # we apply bi to the chain using x_indexes
            res[x_index]=bi[bi_index]
        result.append(''.join(res))
    return result

def lstring2binary(ls):
    # return a binary out of a list of string
    return int(''.join(ls),2)

def bin2str(i,z=36):
    # return a string out of a integer
    return ''.join(bin(int(i))[2:].zfill(z))

with open('input14.txt') as f:
    lines = f.read().splitlines()
    instructions = []
    c = {}
    for l in lines:
        # ugly line parsing is ugly
        var = l.split(' ')[0]
        value = l.split(' ')[-1]
        if 'mask' in var:
            instructions.append(c)
            c = {}
            c['mask'] = value
            c['oper'] = {} 
        else:
            # more ugly line parsing for the memory addr
            c['oper'][int(var[4:-1])] = bin2str(value)
    # our instructions has been parsed into an easily iterable format, we could speed up things by looping only once
    # be this might cause brain damage...
    instructions.append(c)
    res = {}

    for ins in instructions[1:]:
        for addr,v in ins['oper'].items():
            result = [0] * len(ins['mask'])
            for i,bit in enumerate(list(bin2str(addr))):
                # we apply the mask, if it's X it stay X, otherwise we follow instructions
                if ins['mask'][i] =='X':
                    result[i]='X'
                elif int(ins['mask'][i]) == 1:
                    result[i] = '1'
                elif int(ins['mask'][i]) == 0:
                    result[i] = str(bit)
            # at this point we still have X in our binary, we will generate a list out of it
            new_values = xbin2lbin(''.join(result))
            for nv in new_values:
                res[int(''.join(nv),2)]=int(v,2)
    print("tada",sum(res.values()))
