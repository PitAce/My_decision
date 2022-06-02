import re 

def count_words(string):
  
  str_no_marks = re.sub(r'[^\w\s]',' ', string)  # deleting marks
  
  str_list = str_no_marks.lower().split() 
  
  str_dict = {}
  for i in str_list:
      str_dict[i] = str_list.count(i)
  return str_dict
