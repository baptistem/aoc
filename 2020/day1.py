friends = 1

def find_friends(total,expenses):
    overhead = len(expenses)%2
    bigger_expenses = expenses[len(expenses)//2+overhead:]
    smaller_expenses = expenses[:len(expenses)//2+overhead]
    for e in smaller_expenses:
        friend = total-int(e)
        if friend > int(bigger_expenses[-1]):
            pass
        if str(friend) in bigger_expenses:
            return friend,e

with open('input.txt') as f:
    expenses = f.read().splitlines()
    intexpenses = []
    expenses.sort(key=int)
    bigger_expenses = expenses.copy()
    bigger_expenses.reverse()

    smalli = 0
    largei = len(expenses)-1
    small = iter(expenses)
    large = iter(bigger_expenses)
    smallv = int(next(small))
    largev = int(next(large))
    i = -1
    e = iter(expenses)
    total_oper = 0
    total = 0
    while total != 2020:
        total_oper += 1
        value = int(next(e))
        i += 1
        print(f"{largev} {smallv} {value} {total} global")
        if i == smalli:
            continue
        if i == largei:
            break
        total = largev + value
        while (total > 2020):
            total_oper +=1
            print(f"{largev} {smallv} {value} {total} largev")
            try :
                largev = int(next(large))
            except (StopIteration):
                large = iter(bigger_expenses)
                largev = int(next(large))
                largei = len(expenses)-1
                value = int(next(e)) 
                i += 1 
                if i == largei:
                    Error()
                break
            total = largev + value
            largei -= 1
        if i == largei:
            break
        total = smallv + largev + value
        print(f"{largev} {smallv} {value} {total} {i} {smalli} before small")
        while(total < 2020):
            total_oper +=1
            smallv = int(next(small))
            smalli += 1
            total = smallv + largev + value
            print(f"{largev} {smallv} {value} {total} {i} {smalli} small")
            if i == smalli:
                break
        if i == smalli:
            break
        if (total > 2020):
            largev=int(next(large))
            small = iter(expenses)
            smalli = 0
            smallv = int(next(small))
            largei -= 1
            total = smallv + largev + value
            print(f"{largev} {smallv} {value} {total} {i} {smalli} large")
            if largei == i:
                break

    print(smallv+largev+value)
    print(smallv*largev*value)
    print(f"done in {total_oper}")
