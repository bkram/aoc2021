previous = 0
match = 0
with open('input', 'r') as file:
    data = file.read().split('\n')[:-1]
    for i in range(1, len(data)):
        this = data[i:(i + 3)]
        if len(this) == 3:
            window = int(this[0]) + int(this[1]) + int(this[2])
            if window > previous:
                match += 1
            previous = window
    print('Higher windows {}'.format(match))
