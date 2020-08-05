import solution

def test_solution():
    def equivalent_lsts(solnlst, retlst):
        if len(solnlst) != len(retlst):
            return False
        elif solnlst == retlst:
            return True
        else:
            for lst in solnlst:
                if lst not in retlst:
                    return False
            return True

    retlst1 = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    solnlst1 = solution.py_solution().sub_sets([1, 2, 3])
    assert(equivalent_lsts(solnlst1, retlst1)) == True

    retlst2 = [[], [2], [1], [1, 2]]
    solnlst2 = solution.py_solution().sub_sets([1, 2])
    assert(equivalent_lsts(solnlst2, retlst2)) == True

    retlst3 = [[]]
    solnlst3 = solution.py_solution().sub_sets([])
    assert(equivalent_lsts(solnlst3, retlst3)) == True