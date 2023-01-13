def same_chars(characters):
    '''(str)-> bool
    >>> same_chars('555')
    True
    >>> same_chars('aaaaa')
    True
    >>> same_chars('COMP')
    False
    >>> same_chars('aaAa')
    False
    '''
    
    for char in characters:
        if char != characters[0] or len(characters) <1:
            return False
    
    return True

def get_txt_msg(str_of_digits, mapping_dictionary):
    '''(str,dict)-> str
    >>> d = {2 : ['A', 'B', 'c'], 7 : ['p', 'q', 'r', 'S']}
    >>> get_txt_msg('222 2 777', d)
    'cAr'
    
    >>> get_txt_msg('11 2 5', d)
    Traceback (most recent call last):
    ValueError: Invalid input string
    
    >>> get_txt_msg('77 2222', d)
    Traceback (most recent call last):
    ValueError: Invalid input string
    
    
    >>> map_two = {0 : ['a ', 'the ', 'an '], 1 : ['lion ', 'bear ', 'cat '], 2 : ['is ', 'are ', 'has '], 3 : ['over ', 'under ', 'below ', 'in '], 4 : ['table ', 'forest ', 'tree ', 'cave ']}
    >>> s = '00 1 2 33 00 444'
    >>> get_txt_msg(s, map_two)
    'the lion is under the tree '
    
    >>> map_one = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], 5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z'], 0: [' ']}
    >>> code = '222 666 3 444 66 4 0 444 7777 0 333 88 66'
    >>> msg = get_txt_msg(code, map_one)
    >>> msg
    'coding is fun'
    '''
    
    sentence =''
    list_of_digits = str_of_digits.split()
    
    for digits in list_of_digits:
        invalid = False
        #digit is in dict and has same characters
        if same_chars(digits) and digits.isdecimal() and int(digits[0]) in mapping_dictionary:
            #checks if She was well-articulated, with a good tone of voice and she kept eye contact with the audience.
            if len(digits) > len (mapping_dictionary[int(digits[0])]):
                invalid = True
                break
            else:
                #value of the dict
                list_of_letters = mapping_dictionary[int(digits[0])]
                letter = list_of_letters[len(digits)-1]
                sentence += letter
        else:
            invalid = True
            break
            
    if invalid:
        raise ValueError ('Invalid input string')
    return sentence

    
