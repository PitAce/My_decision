def max_odd(list_mas):

              #check for nested lists and selecting numbers (like in task_2):
    sort_list = []
  
    for i in list_mas:
        if type(i) == list:
            list_mas.extend(i) 
        else:
            if type(i)==int or type(i)==float:
                sort_list.append(i)
  
  
    odd_list = [int(i) for i in sort_list if i% 2!=0]  #list with odd int
  
    if odd_list:
        return(max(odd_list))
    else:
        return(None)
