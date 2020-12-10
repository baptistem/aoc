from collections import defaultdict
with open('input10.txt') as f:
    lines = f.readlines()
    ilines = [ int(l.strip()) for l in lines ]
    ilines.append(0)
    ilines.sort()
    # one-liner warning ! we could do a append ... but this is faster
    # we build a diff list of the substraction to count 3 and 1
    difflist = [ ilines[i+1] - ilines[i] for i in range(len(ilines)-1)]
    difflist.append(3) # this if for the computer, remember?
    # end of part A!
    print('paf',(difflist.count(1))*(difflist.count(3)+1))

    possible = defaultdict(int) # failsafe dic which yield 0 if the key is unknown
    possible[ilines[0]] = 1 # ilines[0] = 0, we added this ourself, if we plug nothing it still count as 1
    # ok here is the idea
    # we don't need to go over all the branch and count the number of possibilities to be here it's too much
    # think about your poor cpu, poor dude
    # so instead we will remember the weight of each branch
    # and add it to the next branch if possible
    # at the end of the tree, the branch will be BIG that it will BREAK<esc>dd
    # once reach the latest value, we can get the number of permutation (weight) to be here
    for i in ilines:
        for j in range(1,4):
            if i+j in ilines:
                possible[i+j] += possible[i] # for each possibility we add the weight of the current branch we are on
    # end of part B
    # finaly we print the weight of the latest value as it is the one relevant here!
    print("tada",possible[ilines[-1]])
