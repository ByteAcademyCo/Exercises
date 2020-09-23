def test_solution():
    from solution import Vector3D

    vec1 = Vector3D(-4, -4, 1)
    vec2 = Vector3D(4, 4, 1)
    vec3 = Vector3D(4, 4, 1)

    assert not (vec1 == vec2)
    assert not (vec1 == vec3)
    assert vec3 == vec3
    assert vec1 == vec1
