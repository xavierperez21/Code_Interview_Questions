def checkPermutation(str1, str2):
    # Both of the strings must have the same length to be permutations
    if (len(str1) != len(str2)) : return False

    # Creating a hash table (dictionary) so we can find if the other string has the same characters in O(1) time
    char_dict = {}

    for c in str1:
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1

    for c in str2:
        if c not in char_dict:
            return False
        else:
            char_dict[c] -= 1
            if char_dict[c] < 0:
                return False

    return True


if __name__ == "__main__":
    print(checkPermutation("hoola ", " hooola"))