def serializer():
    file = open("input.txt", "r")
    trajectory = []
    for f in file:
        trajectory.append(f[0:-1])
    return trajectory

def part_one(trajectory, x_step, y_step):

    width = len(trajectory[0]) - 1
    height = len(trajectory) - 1
    curr_x = 0
    curr_y = 0
    trees = 0
    
    while curr_x <= height:
        if trajectory[curr_x][curr_y] == '#':
            trees += 1
        curr_x += x_step
        curr_y += y_step
        if curr_y + 3 > width:
            curr_y = curr_y - width - 1
    return trees


def part_two(trajectory):
    mult = 1
    mult *= part_one(trajectory, 1, 1)
    mult *= part_one(trajectory, 1, 3)
    mult *= part_one(trajectory, 1, 5)
    mult *= part_one(trajectory, 1, 7)
    mult *= part_one(trajectory, 2, 1)
    return mult


if __name__ == '__main__':
    trajectory = serializer()
    print(part_two(trajectory))