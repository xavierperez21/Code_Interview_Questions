# O(N)
import unittest

# -------------- First method: Using a hash table to count each letter -----------------------
def isPalindromePermutation(string):
    if len(string) <= 1: return False

    # Avoiding uppercase
    string = string.lower()

    char_dict = {}
    for c in string:
        # We don't consider blank spaces
        if c == " ": continue

        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    
    # Checking how many keys has an odd quantity
    odd_count = 0
    for key in char_dict:
        if char_dict[key] % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1


# -------------- Second method by not using extra memory (not finished) -------------------
# def isPalindromePermutation(string):
#     if len(string) <= 1: return False

#     sorted_string = sorted( string.lower() )
#     current = ""
#     count = 0
#     odd_count = 0
#     for c in sorted_string:
#         if c != current:
#             current = c
#             if count % 2 != 0:
#                 odd_count += 1
#             count = 1
#         else:
#             count += 1

#     return odd_count <= 1


class Test(unittest.TestCase):
    dataT = [('abba'), ('sfssfdd'), ('Taco Coa'), ('Anita lava la tina')]
    dataF = [('abvdhba'), ('{swrsdo+9ic'), ('hola')]

    def test_palindrome(self):
        # true check
        for test_string in self.dataT:
            actual = isPalindromePermutation(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = isPalindromePermutation(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()