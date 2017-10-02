from math import radians, sin, cos, sqrt


def position(p, cmd, val):
    if cmd == 'turn':
        p[2] += val
    else:
        p[0] += val * cos(radians(p[2]))
        p[1] += val * sin(radians(p[2]))


def dist_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def run_it(t):
    pos_coll = []
    x_sum = 0.0
    y_sum = 0.0
    for i in range(t):
        inp = raw_input()
        s= inp.split()
        pos = list(map(float, s[:2]))
        direction = s[2:]
        it = iter(direction)
        next(it)
        pos.append(float(next(it)))
        for j in range(len(direction) // 2 - 1):
            position(pos, next(it), float(next(it)))
        pos_coll.append(tuple(pos[:2]))
        x_sum += pos[0]
        y_sum += pos[1]
    average = (x_sum / len(pos_coll), y_sum / len(pos_coll))
    dist = 0
    for p in pos_coll:
        d = dist_squared(p, average)
        if d > dist:
            dist = d
    print("{:.4f} {:.4f} {:.4f}".format(average[0], average[1], sqrt(dist)))


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        run_it(n)
