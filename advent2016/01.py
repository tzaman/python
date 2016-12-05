from collections import namedtuple

Vec = namedtuple('Vec', 'x y')
add = lambda v1, v2: Vec(v1.x + v2.x, v1.y + v2.y)
ways = (Vec(1, 0), Vec(0, 1), Vec(-1, 0), Vec(0, -1))

def solve(directions, part2=False):
    position = Vec(0, 0)
    saved = {position}
    orientation = 0

    for d in directions:
        orientation += 1 if d[0]=='R' else -1
        orientation %= 4
        for step in range(int(d[1:])):
            position = add(position, ways[orientation])
            if part2 and position in saved:
                return abs(position.x) + abs(position.y)
            saved.add(position)

    return abs(position.x) + abs(position.y)


if __name__ == '__main__':
    directions = open('01.input').read().split(', ')
    assert solve(['R2', 'L3']) == 5
    assert solve(['R2', 'R2', 'R2']) == 2
    assert solve(['R5', 'L5', 'R5', 'R3']) == 12
    print(solve(directions))

    assert solve(['R8', 'R4', 'R4', 'R8'], part2=True) == 4
    print(solve(directions, part2=True))
