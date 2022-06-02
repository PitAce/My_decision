def connect_dicts(dict1, dict2):
    
    sum_value1 = (sum(dict1.values()))
    sum_value2 = (sum(dict2.values())) 
                  # Creating a new dict, according the rules:
    new_dict = {}
    
    def f_dict(x):
        for key,value in x.items():
            if (value > 10) and (key not in new_dict):
                new_dict[key] = value
                  # Priority check
    if (sum_value2 > sum_value1) or (sum_value2 == sum_value1):
        f_dict(dict2)
        f_dict(dict1)
    else:
        f_dict(dict1)
        f_dict(dict2)
        
                  # Sorting the new dictionary:
    sort_dict = {}
    sort_values_nd = sorted(new_dict.values())
    
    for i in sort_values_nd:
        for key in new_dict.keys():
            if new_dict[key] == i:
                sort_dict[key] = i
    return sort_dict
