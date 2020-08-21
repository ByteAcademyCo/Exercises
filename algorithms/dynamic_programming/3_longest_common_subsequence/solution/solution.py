def longest_common_subseq(str1, str2):
    length_1 = len(str1)
    length_2 = len(str2)
    Length = [[None]*(length_2 + 1) for i in range(length_1 + 1)]
    for i in range(length_1 + 1):
        for x in range(length_2 + 1):
            if i == 0 or x == 0:
                Length[i][x] = 0
            elif str1[i-1] == str2[x-1]:
                Length[i][x] = Length[i-1][x-1] + 1
            else:
                Length[i][x] = max(Length[i-1][x], Length[i][x-1])
    return Length[length_1][length_2]