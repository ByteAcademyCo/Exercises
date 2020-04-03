# Write a function called permutations that consumes a list of numbers lon and returns a list of integers containing all the permutations of lon. The order of the permutations don't matter
# ie. permutations([1,2,3]) -> [123, 132, 213, 231, 312, 321]

class Tree:
    def __init__(self, lon): #[1,2,3,4,5]
        self.children = []
        for i in lon:
            node = Node(i)
            self.children.append(node)
            copy = list(lon)
            copy.remove(i)
            node.gen_children(copy)

    def get_perms(self):
        perms = []
        for i in range(len(self.children)):
            l = self.children[i].get_perms()
            result = filter(lambda x: len(str(x)) == len(self.children), l)
            perms.extend(list(result))
        return perms

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def gen_children(self, lon):
        if lon:
            for num in lon:
                node = Node(int(str(self.val) + str(num)))
                self.children.append(node)
                copy = list(lon)
                copy.remove(num)
                node.gen_children(copy)

    def get_perms(self):
        if self.children == []:
            return [self.val]
        else:
            first_child = self.children[0]
            self.children = self.children[1:]
            return first_child.get_perms() + self.helper(self.children)
    def helper(self, lon):
        if lon == []:
            return []
        else:
            return self.get_perms() + self.helper(lon[1:])


def permutations(lon):
    perm_tree = Tree(lon)
    perms = perm_tree.get_perms()
    return perms

import pytest
def test_permutations():
    L = [1,2,3]
    perms = permutations(L)
    return True if [123, 132, 213, 231, 312, 321] in perms else False

