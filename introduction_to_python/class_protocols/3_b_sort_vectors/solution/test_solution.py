def test_solution():
    from solution import Vector3D, sort_vectors

    vec1 = Vector3D(1, 5, 3)
    vec2 = Vector3D(4, 4, 1)
    vec3 = Vector3D(1, 5, 2)
    vec4 = Vector3D(4, 4, 1)
    vect_lst = [vec1, vec2, vec3, vec4]
    sorted_lst = [vec3, vec2, vec4, vec1]
    ret_lst = sort_vectors(vect_lst)

    for r, s in zip(ret_lst, sorted_lst):
        assert str(r) == str(s)
