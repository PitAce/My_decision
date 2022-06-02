
def coincidence(list_mas=[], range_row=None):
    	
              #checking for missing param.
    if not list_mas or not range_row:
        return([])
    
              #check for nested lists and selecting numbers:
    sort_list, return_list  = [], []
  
    for i in list_mas:
        if type(i) == list:
            list_mas.extend(i) 
        else:
            if type(i)==int or type(i)==float:
                sort_list.append(i)
        
             #defining elements from sort_list that included in range_row:
    ranList = [i for i in range_row]      
    for i in sort_list:
        if ranList[0] <= i <= ranList[-1]:
            return_list.append(i)
    return(return_list)   
