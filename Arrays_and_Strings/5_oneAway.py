# O(N)
import unittest

def oneAwayEdit(str1, str2):
    if (len(str1) == len(str2)):
        return checkReplacement(str1, str2)

    elif (len(str1) + 1 == len(str2)):
        return checkInsertion(str1, str2)

    elif (len(str1) - 1 == len(str2)):
        return checkInsertion(str2, str1)

    return False


def checkReplacement(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            if(foundDifference):
                return False

            foundDifference = True
    
    return True


def checkInsertion(str1, str2):
    index1 = 0
    index2 = 0
    while (index1 < len(str1) and index2 < len(str2)):
        if (str1[index1] != str2[index2]):
            if (index1 != index2):
                return False
            index2 += 1
        
        index1 += 1
        index2 += 1
    
    return True


class Test(unittest.TestCase):
    dataT = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale')]
    dataF = [('pale', 'bake'), ('pale', 'elp')]

    def test_one_away(self):
        # true check
        for str1, str2 in self.dataT:
            actual = oneAwayEdit(str1, str2)
            self.assertTrue(actual)

        # false check
        for str1, str2 in self.dataF:
            actual = oneAwayEdit(str1, str2)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()