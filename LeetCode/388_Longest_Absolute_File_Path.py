# Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:



# Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

# In text form, it looks like this (with ⟶ representing the tab character):

# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
# If we were to write this representation in code, it will look like this: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line and tab characters.

# Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.

# Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note that the testcases are generated such that the file system is valid and no file or directory name has length 0.

 

# Example 1:


# Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# Output: 20
# Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
# Example 2:


# Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# Output: 32
# Explanation: We have two files:
# "dir/subdir1/file1.ext" of length 21
# "dir/subdir2/subsubdir2/file2.ext" of length 32.
# We return 32 since it is the longest absolute path to a file.
# Example 3:

# Input: input = "a"
# Output: 0
# Explanation: We do not have any files, just a single directory named "a".
 

# Constraints:

# 1 <= input.length <= 104
# input may contain lowercase or uppercase English letters, a new line character '\n', a tab character '\t', a dot '.', a space ' ', and digits.
# All file and directory names have positive length.







# Brute force:
class Solution:
    def lengthLongestPath(self, input: str) -> int:

        # Each node: {"name": ..., "children": [...]}
        root = {
            "name": "",
            "children": []
        }

        # Stack stores nodes at each depth
        stack = [root]

        # Build the tree
        for line in input.split('\n'):

            depth = line.count('\t')
            name = line[depth:]

            node = {
                "name": name,
                "children": []
            }

            # Parent is at depth - 1
            parent = stack[depth]

            parent["children"].append(node)

            # Current node becomes available at next depth
            if len(stack) > depth + 1:
                stack[depth + 1] = node
            else:
                stack.append(node)

        # DFS to find longest file path
        def dfs(node, current_path):

            # Root node
            if node["name"] == "":
                path = ""
            else:
                if current_path:
                    path = current_path + "/" + node["name"]
                else:
                    path = node["name"]

            # If it's a file
            if "." in node["name"]:
                return len(path)

            max_length = 0

            # Visit children
            for child in node["children"]:
                max_length = max(
                    max_length,
                    dfs(child, path)
                )

            return max_length

        return dfs(root, "")







# Optimal:
class Solution:
    def lengthLongestPath(self, input: str) -> int:

        # path_length[i] = length of path up to depth i
        path_length = [0] * (len(input) + 1)

        max_length = 0

        for line in input.split('\n'):

            # Number of tabs = depth
            depth = line.count('\t')

            # Remove tabs to get actual name
            name = line[depth:]

            # Current path length
            path_length[depth + 1] = (
                path_length[depth] + len(name) + 1
            )

            # If it's a file
            if '.' in name:
                # -1 because we added an extra '/'
                max_length = max(
                    max_length,
                    path_length[depth + 1] - 1
                )

        return max_length