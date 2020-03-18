def is_anagram(text1, text2):
    if len(text1) != len(text2) or len(text1) == 0 or len(text2) == 0:
        return print("Invalid input!")
    dict = {}

    # Record number of chars in text1
    for char in text1.upper():
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    # Look up each text2 char in dict
    for char in text2.upper():
        if char not in dict:
            return print("Not an anagram!")
        dict[char] -= 1

    sum = 0
    # If the sum of the remaning counts in dict != 0, then they are not anagrams
    for key in dict:
        sum += dict[key]
    if sum != 0:
        return print("Not an anagram!!")
    return print("Is an anagram!")