

def max_num(list):
    list.sort()
    return list[-1]


print(max_num([1, 5, 9]))


def multiList(list):
    total = 0
    for i in range(3):
        total = total + list[i]
    return total

print(multiList([1, 5, 9]))


def rev_string(string):
    return string[::-1]

print(rev_string('Hello'))

def within_range(x,y,z):
    for x in range(z):
        if x == y:
            return True 
    return False

print(within_range(1,2,5))