# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For
# example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to
# a file in the abstracted file system. If there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.

class LongestABSPathNode:
    def __init__(self, file_name, is_file=False, children=[]):
        assert len(file_name) > 0
        self.file_name = file_name
        self.name_length = len(file_name)
        self.is_file = is_file
        self.children = children

    def add_children(self, new_children):
        self.children = self.children + new_children

    def add_child(self, new_child):
        self.children.append(new_child)




def longest_abs_path(fs: str):
    """
    Given a string that represent a file system, find the longest absolute path
    :param fs:
    :return:
    """

    # TODO: parse the fs str one time and build a graph/tree, where nodes contain the text length of that file/dir
    #  from the tree root, dfs and find a path where the nodes contained the most text length, and path ends on a file

    # this is not my own solution, I struggled to build the file tree from the given string
    # see https://www.youtube.com/watch?v=Ad9Qqhy43fE

    lines = fs.split('\n')

    max_len = 0
    depth_map = {0: 0}
    for line in lines:
        path = line.split('\t')[-1]
        depth = len(line) - len(path)

        if "." in path:
            max_len = max(max_len, depth_map[depth] + len(path))
        else:
            depth_map[depth + 1] = depth_map[depth] + len(path) + 1

    return max_len


assert longest_abs_path("dir\n\tsubdir1\n\tsubdir2") == 0
assert longest_abs_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
assert longest_abs_path("dir\n\tsubdir1\n\t\tfile.txt\n\tsubdir2\n\t\tfile.ext") == 20
assert longest_abs_path(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t" +
    "subsubdir2\n\t\t\tfile2.ext") == 32