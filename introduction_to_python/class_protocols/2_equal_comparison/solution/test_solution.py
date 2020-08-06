def test_solution():
    import solution

    vec1 = solution.Vector3D(-4, -4, 1)
    vec2 = solution.Vector3D(4, 4, 1)
    vec3 = solution.Vector3D(4, 4, 1)

    assert not (vec1 == vec2)
    assert not (vec1 == vec3)
    assert vec3 == vec3
    assert vec1 == vec1