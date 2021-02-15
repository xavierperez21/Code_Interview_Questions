def hasUniqueChars(sentence):
    n = len(sentence)
    # The ASCII code only has 128 unique characters
    if n > 128:
        return False

    # Creating an array of 128 False values
    char_set = [False for _ in range(128)]
    for c in sentence:
        # Obtaining ASCII value of the character
        val = ord(c)
        if (char_set[val]):
            return False
        char_set[val] = True
    
    return True


if __name__ == "__main__":
    sentence = input("Check if your sentence has unique chars: ")
    print(hasUniqueChars(sentence))