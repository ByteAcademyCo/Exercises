def test_solution():
    import solution
    import math

    vec1 = solution.Vector3D(1, 5, 3)
    vec2 = solution.Vector3D(4, 4, 1)
    vec3 = solution.Vector3D(1, 5, 2)

    assert vec1.magnitude() == math.sqrt(35)
    assert vec2.magnitude() == math.sqrt(33)
    assert vec3.magnitude() == math.sqrt(30)