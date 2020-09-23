def test_solution():
        import solution

        n1 = solution.ListNode(5)
        n2 = solution.ListNode(6, n1)
        n3 = solution.ListNode (4, n2)
        n4 = solution.ListNode(1, n3)
        llst = solution.LinkedList(n4)

        llst2 = solution.LinkedList(n1)

        r1 = solution.ListNode(6)
        r2 = solution.ListNode(5, r1)
        r3 = solution.ListNode(4, r2)
        r4 = solution.ListNode(1, r3)
        returnlst = solution.LinkedList(r4)

        llst.sort_ll()
        llst2.sort_ll()

        assert (llst.head.value == returnlst.head.value and
        llst.head.next.value == returnlst.head.next.value and
        llst.head.next.next.value == returnlst.head.next.next.value and
        llst.head.next.next.next.value == returnlst.head.next.next.next.value)
        
        assert (llst2.head.value == llst2.head.value and llst2.head.next == None)
    
