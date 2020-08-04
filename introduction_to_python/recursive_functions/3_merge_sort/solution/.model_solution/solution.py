def custom_sort(num_list):
    if len(num_list)>1:                 
        mid = int(len(num_list)/2)      
        lefthalf = num_list[:mid]       
        righthalf = num_list[mid:]     

        custom_sort(lefthalf)
        custom_sort(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                num_list[k]=lefthalf[i]
                i=i+1
            else:
                num_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            num_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            num_list[k]=righthalf[j]
            j=j+1
            k=k+1
    return num_list
