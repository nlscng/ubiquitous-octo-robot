'''
brute force: o(n^2)

slightly better:
1.sort, o(n log n)
[2, 1, 0, -1 , -2], k = 1
               *
    2  1  0    -1
    0  -1 -2   -3

res:[[2,1], [1, 0], [0, -1], [-1, -2]]

set:{2, 1, 0, -1}


[2, 1, ,-1 , -2], k = 20
        *
    21  19
   -19  -21
seen_set: {2}, o(2)



[0, -1, -2, 2, 1], k = 1
    *
    0
    -2

res: [[0, -1]]

set: {0}



https://www.linkedin.com/in/maxwellengel/

https://www.linkedin.com/in/nelson-cheng-a142b987/

Elements of Programming in Python
'''


def find_pairs_with_given_difference(arr, k):
    # safety check
    if len(arr) < 2:
        return []

    seen = set(arr)

    res = []
    for one_ele in arr:
        t = k + one_ele
        if t in seen:
            res.append([t, one_ele])

    return res


assert find_pairs_with_given_difference([4, 1], 3) == [[4, 1]]
assert find_pairs_with_given_difference([1,5,11,7], 4) == [[5, 1], [11, 7]]
assert find_pairs_with_given_difference([0,-1,-2,2,1], 1) == [[1, 0], [0, -1], [-1, -2], [2, 1]]
assert find_pairs_with_given_difference([1,7,5,3,32,17,12], 17) == []
