def test_solution():
    import solution

    assert solution.Person("Jane Doe").getName() == "Jane Doe"
    assert solution.Person("Jane Doe").isEmployee() == False
    assert str(solution.Person("Jane Doe")) == 'Person(name=Jane Doe)'

    assert solution.Employee("Jane Doe").getName() == "Jane Doe"
    assert solution.Employee("Jane Doe").isEmployee() == True
    assert str(solution.Employee("Jane Doe")) == 'Employee(name=Jane Doe)'


    
   