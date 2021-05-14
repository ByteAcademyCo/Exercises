g_dict = {3: "Triangle" , 4: "Quadrilateral" , 5: "Pentagon", 6: "Hexagon", 7: "Heptagon", 
8: "Octagon", 9: "Nonagon"}

g_lst = []
while ((g_int := int(input("enter your number"))) in range(3,10)):
    g_lst.append(g_dict[g_int])
