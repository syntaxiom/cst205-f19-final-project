amst_list = ["Amsterdam", "Netherlands", "books", "library", "museum"]

def wordist(s):
    if s[1] == s[4]:
        return True
    else:
        return False

result_list2 = list(filter(wordist, amst_list))

print(result_list2) 