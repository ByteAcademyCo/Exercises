from provided_code import L

if L[0] >= L[1] and L[0] >= L[2] and L[0] >= L[3] and L[0] >= L[4]:
    LIST_MAX = L[0]
elif L[1] >= L[0] and L[1] >= L[2] and L[1] >= L[3] and L[1] >= L[4]:
    LIST_MAX = L[1]
elif L[2] >= L[0] and L[2] >= L[1] and L[2] >= L[3] and L[2] >= L[4]:
    LIST_MAX = L[2]
elif L[3] >= L[0] and L[3] >= L[1] and L[3] >= L[2] and L[3] >= L[4]:
    LIST_MAX = L[3]
elif L[4] >= L[0] and L[4] >= L[1] and L[4] >= L[2] and L[4] >= L[3]:
    LIST_MAX = L[4]
else:
    LIST_MAX = 'error'
