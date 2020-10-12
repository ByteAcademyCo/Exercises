def test_solution():
    from solution import Vector3D

    vector1 = Vector3D(1, 2, 3)
    assert vector1.x == 1
    assert vector1.y == 2
    assert vector1.z == 3

    vector2 = Vector3D(y=1, z=2)
    assert vector2.x == 0
    assert vector2.y == 1
    assert vector2.z == 2

    vector3 = Vector3D()
    assert vector3.x == 0
    assert vector3.y == 0
    assert vector3.z == 0
