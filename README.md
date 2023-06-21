# Keypad-Decoder
This code is a keypad decoder implemented in Python. It is designed to convert a string of digits into a text message using a provided mapping dictionary. The code consists of two functions:


1)same_chars(characters): This function checks if all characters in a given string are the same. It takes a string (characters) as input and returns a boolean value (True if all characters are the same, False otherwise).

2)get_txt_msg(str_of_digits, mapping_dictionary): This function converts a string of digits to a text message using a mapping dictionary. It takes two arguments: str_of_digits, which is the input string of digits, and mapping_dictionary, which is the dictionary used for mapping digits to corresponding letters. The function iterates through the digits in the input string, performing various checks. If any of the checks fail, a ValueError is raised. If all checks pass, the function retrieves the corresponding letter from the mapping dictionary based on the first digit of the current group of digits and appends it to the sentence. The resulting text message is returned at the end.

The code includes informative docstrings that describe the purpose of each function, the arguments they accept, the expected return values, and any potential exceptions that can be raised. This helps users understand how to use the code and what to expect from it.
