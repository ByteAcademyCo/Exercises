def test_solution():
    from solution import Employee, give_raises

    emp1 = Employee("John", 1, 45000, 8)
    emp2 = Employee("Jane", 2, 22000, 1)
    emp3 = Employee("Marie", 3, 90000, 10)

    give_raises([emp1, emp2, emp3])

    emp4 = Employee("Mark", 3, 90000, 5)
    give_raises([emp4])

    assert emp1.salary == 53000
    assert emp2.salary == 27000
    assert emp3.salary == 100000
    assert emp4.salary == 95000
