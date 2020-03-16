def is_palindrome(text):
    # check that string is valid
    text = str(text)
    if len(text) == 0:
        return print("Input is not valid!")

    # store length of string and middle character (rounded down)
    length = len(text)
    mid = int(length / 2)

    # iterate until middle character from beginning and end
    for i in range(0, mid):
        if text[i] != text[length-i-1]:
            return print("Not a palindrome!")
    return print("Is a palindrome!")
