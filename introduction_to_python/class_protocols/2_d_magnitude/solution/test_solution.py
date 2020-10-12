def test_solution():
    from solution import Vector3D
    import math

    vec1 = Vector3D(1, 5, 3)
    vec2 = Vector3D(4, 4, 1)
    vec3 = Vector3D(1, 5, 2)

    assert abs(vec1) == math.sqrt(35)
    assert abs(vec2) == math.sqrt(33)
    assert abs(vec3) == math.sqrt(30)
