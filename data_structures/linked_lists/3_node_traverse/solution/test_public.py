def test_solution(monkeypatch):
    ret_val = []

    def g(num):
        ret_val.append(num)

    monkeypatch.setattr("builtins.print", g)

    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(1)
    e2 = Node(2)
    items.head.next = e2
    items.traverse()

    assert ret_val[0] == 1
    assert ret_val[1] == 2
