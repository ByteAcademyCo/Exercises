def test_solution():
    from solution import cosette

    assert cosette.name == "Cosette Rodger"
    assert cosette.employee_id == 1
    assert cosette.salary == 100000
    assert cosette.years_at_company == 4
