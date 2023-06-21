def same_chars(characters):
    """
    Check if all characters in a string are the same.

    Args:
        characters (str): The input string.

    Returns:
        bool: True if all characters are the same, False otherwise.
    """
    return all(char == characters[0] for char in characters)

def get_txt_msg(str_of_digits, mapping_dictionary):
    """
    Convert a string of digits to a text message based on a mapping dictionary.

    Args:
        str_of_digits (str): The input string of digits.
        mapping_dictionary (dict): The mapping dictionary.

    Returns:
        str: The resulting text message.

    Raises:
        ValueError: If the input string is invalid.
    """
    sentence = ''
    list_of_digits = str_of_digits.split()

    for digits in list_of_digits:
        if not (same_chars(digits) and digits.isdecimal() and int(digits[0]) in mapping_dictionary):
            raise ValueError('Invalid input string')

        if len(digits) > len(mapping_dictionary[int(digits[0])]):
            raise ValueError('Invalid input string')

        list_of_letters = mapping_dictionary[int(digits[0])]
        letter = list_of_letters[len(digits)-1]
        sentence += letter

    return sentence
