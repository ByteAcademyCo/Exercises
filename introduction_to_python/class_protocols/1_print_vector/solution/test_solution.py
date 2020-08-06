def test_solution():
    import solution

    vector1 = solution.Vector3D(1, 2, 3)
    assert str(vector1) == '(x = 1, y = 2, z = 3)'

    vector2 = solution.Vector3D(y=1, z=2)
    assert str(vector2) == '(x = 0, y = 1, z = 2)'

    vector3 = solution.Vector3D()
    assert str(vector3) == '(x = 0, y = 0, z = 0)'