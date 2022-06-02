def multiply_numbers(inputs = None):
  
  no_numb, numb = None, '1234567890'

  all_string = str(inputs)
  result = 1
  
  for i in all_string:
    if i in numb:
      result *= int(i)
      no_numb = i
     
  if no_numb:
    return(result)
  return no_numb
