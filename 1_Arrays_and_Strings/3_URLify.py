
# ----------- First Try-----------
# def listToString(string):
#     str1 = ""

#     for c in string:
#         str1 += c

#     return str1
    

# def URLify(string, true_length):
#     # Convert the string to an array
#     string = [char for char in string]
    
#     # End of the true string
#     end = true_length - 1


#     for i in range(true_length):
#         # if the char is a blank space
#         if ord(string[i]) == 32:
#             for j in range(end-i):
#                 # Shifting 2 spaces all the characters from the end to the begining. That's why we substract j ([end - j])
#                 string[end+2-j] = string[end-j]

#             # Once we have space we can add the special characters
#             string[i] = '%'
#             string[i+1] = '2'
#             string[i+2] = '0'

#             # We have to modify the end of the true string for the next blank space we find
#             end = end + 2

#     return listToString(string)


# ---------------- Second Try (optimal solution) -------------------
# O(N)
def replaceSpaces(string, true_length):
    string = list(string)

    index = len(string)
    for i in range(true_length - 1, -1, -1):
        print(i)
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index = index - 3
        else:
            string[index - 1] = string[i]
            index = index - 1

    return "".join(string)


if __name__ == "__main__":
    # print(URLify("Mr John Smith    ", 13))
    print(replaceSpaces("Mr John Smith    ", 13))