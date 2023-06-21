# Keypad-Decoder
This code is a keypad decoder implemented in Python. The purpose of the code is to convert a string of digits into a corresponding text message based on a provided mapping dictionary.

The code consists of two functions: same_chars() and get_txt_msg().

The same_chars() function checks whether all characters in a string are the same. It iterates through each character in the input string and compares it to the first character. If any character is different or the length of the string is less than 1, the function returns False. Otherwise, it returns True. This function is used to validate if a string of digits has the same characters.

The get_txt_msg() function is the main part of the code. It takes two parameters: str_of_digits (the input string of digits) and mapping_dictionary (a dictionary that maps each digit to a list of corresponding letters or words).

The function starts by initializing an empty string called sentence to store the resulting text message. The input string of digits is split into a list of individual digit strings using the split() method.

Next, the function iterates through each element (digit string) in the list. For each digit, it performs several checks. It verifies if the digit is in the mapping dictionary and if all characters in the digit string are the same and numeric. If these conditions are met, it retrieves the list of letters corresponding to the digit from the mapping dictionary. It then selects the letter based on the length of the digit string and appends it to the sentence string.

If any of the checks fail, indicating an invalid input string, the function raises a ValueError with an appropriate error message.

Finally, the function returns the resulting sentence string, which represents the decoded text message.

The code includes some examples as docstrings, demonstrating how to use the functions and providing expected output for different input scenarios.

Overall, this code provides a simple and efficient way to convert a string of digits into a text message using a mapping dictionary. It can be useful for applications involving keypads or numerical input methods for generating text messages.
