def test_solution():
    import solution

    vec1 = solution.Vector3D(1, 2, 0)
    vec2 = solution.Vector3D(y=1, z=3)
    vec3 = solution.Vector3D()

    assert (vec1 - vec2).x == 1
    assert (vec1 - vec2).y == 1
    assert (vec1 - vec2).z == -3

    assert (vec1 - vec3).x == 1
    assert (vec1 - vec3).y == 2
    assert (vec1 - vec3).z == 0