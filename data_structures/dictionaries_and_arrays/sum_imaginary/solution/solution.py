def sum_imaginary(ilst):
    real = 0
    img = 0
    for tup in ilst:
        real += tup[0]
        img += tup[1]
    return (real, img)