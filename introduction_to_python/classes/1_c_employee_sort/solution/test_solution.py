def test_solution():
    from solution import Employee, sort_employees

    emp1 = Employee("John", 1, 45000, 8)
    emp2 = Employee("Jane", 2, 22000, 1)
    emp3 = Employee("Marie", 3, 90000, 10)
    emp4 = Employee("Mark", 3, 90000, 5)

    assert sort_employees([emp1, emp2, emp3, emp4]) == ["Jane", "John", "Marie", "Mark"]
    assert sort_employees([emp1]) == ["John"]
    assert sort_employees([]) == []
