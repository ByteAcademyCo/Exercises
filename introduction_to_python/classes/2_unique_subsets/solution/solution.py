class py_solution:
    def sub_sets(self, sset):
        return self.subsets1([], sorted(sset))
    def subsets1(self, current, sset):
        if sset:
            return self.subsets1(current, sset[1:]) + self.subsets1(current + [sset[0]], sset[1:])
        return [current]