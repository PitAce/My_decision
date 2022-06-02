def combine_anagrams(words_array):
  
    result = []
    
    for i in words_array:
        anagram_group = []
        for j in words_array:
            if  sorted(i.lower()) == sorted(j.lower()):
                anagram_group.append(j)
        if anagram_group not in result:
            result.append(anagram_group)
    return(result)
    
    
'''      # Такое решение было изначально, 
      # т.к на момент решения как раз изучал регулярные выражения

import re

def combine_anagrams(words_array):
  
  str_array = ' '.join(words_array).lower()
  result = []
  
  for i in words_array:
    anagram_group  = re.findall("[%s]{%s}" %(i.lower(),len(i)) , str_array)
    if anagram_group and (anagram_group  not in result):
      result.append(anagram_group )
  return(result)
'''
