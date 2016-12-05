
def solve(directions):
    ways = ((1, 0), (0, 1), (-1, 0), (0, -1))
    position = [0, 0]
    orientation = 0

    for d in directions:
        orientation += 1 if d[0]=='R' else -1
        orientation %= 4
        position[0] += ways[orientation][0] * int(d[1:])
        position[1] += ways[orientation][1] * int(d[1:])

    return abs(position[0]) + abs(position[1])

def second(directions):
    ways = ((1, 0), (0, 1), (-1, 0), (0, -1))
    position = [0, 0]
    saved = set()
    orientation = 0

    for d in directions:
        orientation += 1 if d[0]=='R' else -1
        orientation %= 4
        for step in range(int(d[1:])):
            position[0] += ways[orientation][0]
            position[1] += ways[orientation][1]
            if tuple(position) in saved:
                return abs(position[0]) + abs(position[1])
            saved.add(tuple(position))
    


if __name__ == '__main__':
    directions = [d.strip(',') for d in open('1.input').read().split()]
    assert solve(['R2', 'L3']) == 5
    assert solve(['R2', 'R2', 'R2']) == 2
    assert solve(['R5', 'L5', 'R5', 'R3']) == 12
    print(solve(directions))

    assert second(['R8', 'R4', 'R4', 'R8']) == 4
    print(second(directions))
