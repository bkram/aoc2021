previous = 0
match = 0
with open('input', 'r') as file:
    data = file.read().split('\n')[1:-1]
    for a in data:
        if int(a) > previous:
            match += 1
        previous = int(a)
    print('Higher {}'.format(match))
