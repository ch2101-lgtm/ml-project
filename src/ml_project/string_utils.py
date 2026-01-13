def convertToUppercase(string):
    """
    Converts a string to uppercase

    Parameters:
        string (str): string to be converted
    
    Returns:
        uppercaseString (str): string converted to uppercase
    """
    uppercaseString = string.upper()
    
    return uppercaseString


def countVowels(string):
    """
    Counts the number of vowels in a string

    Parameters:
        string (str): string to be counted
    
    Returns:
        nVowels (int): number of vowels in string
    """

    vowels=['A','E','I','O','U']
    nVowels=0
    string=convertToUppercase(string)
    for character in string:
        for vowel in vowels:
            if character == vowel:
                nVowels += 1
    
    return nVowels
