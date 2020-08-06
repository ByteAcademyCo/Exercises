def test_solution():
    import solution

    vec1 = solution.Vector3D(1, 2, 3)
    vec2 = solution.Vector3D(y=1, z=3)
    vec3 = solution.Vector3D()

    assert (vec1 * vec2) == 11
    assert (vec1 * vec3) == 0
    assert (vec1 * vec1) == 14