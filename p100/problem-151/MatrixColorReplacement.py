# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of
# the given pixel and all adjacent same colored pixels with C.
#
# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
#
# B B W
# W W W
# W W W
# B B B
# Becomes
#
# B B G
# G G G
# G G G
# B B B


"""
This at first feels like a dfs search problem.



"""



def replace_color(matrix: list, start: list, color: chr) -> list:
    assert matrix and start and color
    # could use better sanity check, such as checkin for matrix dimensions, start coordinates in bound, etc

    old_color = matrix[start[0]][start[1]]
    seen = set() # set of coordinates that we've seen, regardless of color
    stack = [(start[0], start[1])]
    def get_neighbors(loc: list):
        r, c = loc[0], loc[1]
        n = (r - 1, c) if r > 0 else None
        w = (r, c - 1) if c > 0 else None
        e = (r, c + 1) if c < len(matrix[0]) - 1 else None
        s = (r + 1, c) if r + 1 < len(matrix) else None
        res = []
        for x in [n, s, w, e]:
            if x is not None and x not in seen:
                res.append(x)
        return res

    while len(stack) > 0:
        p = stack.pop()
        seen.add(p)
        if matrix[p[0]][p[1]] == old_color:
            matrix[p[0]][p[1]] = color
        neighbors = get_neighbors(p)
        for one_neighbor in neighbors:
            stack.append(one_neighbor)

    return matrix


m = [['b', 'b', 'w'],
     ['w', 'w', 'w'],
     ['w', 'w', 'w'],
     ['b', 'b', 'b']]

new_color = 'g'
start_loc = [2, 2]

a = [['b', 'b', 'g'],
     ['g', 'g', 'g'],
     ['g', 'g', 'g'],
     ['b', 'b', 'b']]

assert replace_color(m, start_loc, new_color) == a


