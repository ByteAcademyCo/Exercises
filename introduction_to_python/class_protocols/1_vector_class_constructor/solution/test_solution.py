def test_solution():
    import solution

    vector1 = solution.Vector3D(1, 2, 3)
    assert vector1.x == 1
    assert vector1.y == 2
    assert vector1.z == 3

    vector2 = solution.Vector3D(y=1, z=2)
    assert vector2.x == 0
    assert vector2.y == 1
    assert vector2.z == 2

    vector3 = solution.Vector3D()
    assert vector3.x == 0
    assert vector3.y == 0
    assert vector3.z == 0