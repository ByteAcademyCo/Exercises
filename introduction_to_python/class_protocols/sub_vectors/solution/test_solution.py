def test_solution():
    from solution import Vector3D

    vec1 = Vector3D(1, 2, 0)
    vec2 = Vector3D(y=1, z=3)
    vec3 = Vector3D()

    assert (vec1 - vec2).x == 1
    assert (vec1 - vec2).y == 1
    assert (vec1 - vec2).z == -3

    assert (vec1 - vec3).x == 1
    assert (vec1 - vec3).y == 2
    assert (vec1 - vec3).z == 0