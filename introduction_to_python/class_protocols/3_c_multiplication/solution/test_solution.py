def test_solution():
    import solution

    vec1 = solution.Vector3D(1, 2, 3)
    vec2 = solution.Vector3D(y=1, z=3)
    vec3 = solution.Vector3D()
    rvec1 = vec1 * 3
    rvec2 = vec2 * 2
    lvec1 = 3 * vec1

    assert (vec1 * vec2) == 11
    assert (vec1 * vec3) == 0
    assert (vec1 * vec1) == 14
    assert rvec1.x == 3 and rvec1.y == 6 and rvec1.z == 9
    assert rvec2.x == 0 and rvec2.y == 2 and rvec2.z == 6
    assert lvec1.x == 3 and lvec1.y == 6 and lvec1.z == 9
