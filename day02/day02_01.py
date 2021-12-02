horizon, depth = 0, 0
with open('input', 'r') as file:
    for motion, step in [[x[0], int(x[1])] for x in [x.split(" ") for x in file.read().split("\n")]]:
        if motion == "forward":
            horizon += step
        if motion == "up":
            depth -= step
        if motion == "down":
            depth += step
    print("Horizon: {} : Depth: {} Sum: {}".format(horizon, depth, horizon * depth))
