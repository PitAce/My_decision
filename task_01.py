def is_palindrome(string):

            # Converting a string ignoring punctuation marks and registry
    lett_numb = '1234567890qwertyuiopasdfghjklmnbvcxzйцукенгшщзхъфывапролджэюбьтимсчя'
    new_string = ''
    for i in str(string).lower():
        if i in lett_numb:
            new_string += i
      
            # Palindrome check
    if new_string[::-1] == new_string:
        return(True)
    else:
        return(False)

