# Problem Disc: https://leetcode.com/problems/walking-robot-simulation/

new_dir = {
    'North':{-2:'West', -1:'East'},
    'East' :{-2:'North', -1:'South'},
    'South':{-2:'East', -1:'West'},
    'West' :{-2:'South', -1:'North'}
}

def solve(commands, obstacles):
    global new_dir
    point, dir = (0,0), 'North'
    max_dist = 0
    obs = set(map(tuple, obstacles))

    for cmd in commands:
        if cmd < 0:
            dir = new_dir[dir][cmd]
        else:
            for i in range(cmd):
                new_point = move(point, dir)
                if new_point in obs:
                    break
                point = new_point
        x, y = point
        max_dist = max(max_dist, x*x + y*y)

    return max_dist

def move(point, dir):
    if dir == 'East':
        return (point[0]+1, point[1])
    elif dir == 'West':
        return (point[0]-1, point[1])
    elif dir == 'North':
        return (point[0], point[1]+1)
    else:
        return (point[0], point[1]-1)

commands = [4,-1,4,-2,4]
obstacle = [[2,4]]
print(solve(commands, obstacle))

