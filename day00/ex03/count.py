import sys
import string

def text_analyzer(text=None):
    """
        This functions count numbers of upper/lower letters, punctuation spaces
        and letters in a string
    """
    upper_letters = 0
    lower_letters = 0
    punctuation = 0
    spaces = 0
    text_len = 0
    if (text == None):
        print("What is the text ton analyze ?")
        text = sys.stdin.readline()
        spaces -= 1
        text_len = len(text) - 1
    else:
        text_len = len(text)
    for char in text:
        if (char.isupper()):
            upper_letters += 1
        if (char.islower()):
            lower_letters += 1
        if char in (string.punctuation):
            punctuation += 1
        if char.isspace():
            spaces += 1
    print("The text contains {} characters:".format(text_len))
    print("- {} upper letters".format(upper_letters))
    print("- {} lower letters".format(lower_letters))
    print("- {} punctuation marks".format(punctuation))
    print("- {} spaces".format(spaces))
