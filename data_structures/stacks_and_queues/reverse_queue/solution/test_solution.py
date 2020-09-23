def test_solution():
    from solution import Queue

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    retqueue = Queue()
    retqueue.enqueue(3)
    retqueue.enqueue(2)
    retqueue.enqueue(1)

    queue2 = Queue()
    queue2.enqueue(1)

    queue3 = Queue()

    assert queue.reverse_queue() == None
    assert queue == retqueue
    assert queue2.reverse_queue() == None
    assert queue2 == queue2
    assert queue3.reverse_queue() == None
    assert queue3 == queue3
