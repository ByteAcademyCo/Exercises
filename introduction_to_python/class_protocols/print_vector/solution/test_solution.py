def test_solution():
    from solution import Vector3D

    vector1 = Vector3D(1, 2, 3)
    assert str(vector1) == "(x = 1, y = 2, z = 3)"

    vector2 = Vector3D(y=1, z=2)
    assert str(vector2) == "(x = 0, y = 1, z = 2)"

    vector3 = Vector3D()
    assert str(vector3) == "(x = 0, y = 0, z = 0)"
