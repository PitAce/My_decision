def sort_list(list_row):
    if not list_row:
        return(list_row)
        
    maxs, mins, index = max(list_row), min(list_row), 0
    
    for i in list_row:
        if i == maxs:
            list_row[index] = mins
        elif i == mins:
            list_row[index] = maxs
        index += 1
        
    list_row.append(mins)
    return(list_row)
