def test_solution():
    from solution import Vector3D

    vec1 = Vector3D(1, 2, 3)
    vec2 = Vector3D(y=1, z=3)
    vec3 = Vector3D()

    assert (vec1 * vec2) == 11
    assert (vec1 * vec3) == 0
    assert (vec1 * vec1) == 14
