
# day 5

# convert a string to a binary number to a decimal
def txt_to_bin_to_dec(txt,one,zero):
    result = txt.replace(one,'1')
    result = result.replace(zero,'0')
    return int(result,2)


highest = 0
lowest = 9999
seats = {}

with open('input5.txt') as f:
    lines = f.readlines()
    for l in lines:
        row = txt_to_bin_to_dec(l[:7], 'B', 'F') # getting the 7 first
        col = txt_to_bin_to_dec(l[7:], 'R', 'L') # getting the 3 latest
        seat = row*8+col

        # we save the scanned seat for later
        seats[seat]=1
        
        # save the highest
        if seat > highest:
            highest = seat

        # save the lowset
        if seat < lowest:
            lowest = seat

print(highest)
# we check missing seat between the lowest and the highest
for i in range(lowest,highest):
    if i not in seats:
        print(i)
