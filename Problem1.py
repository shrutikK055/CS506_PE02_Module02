def strStr(haystack: str, needle: str) -> int:
    if needle == "":  #if empty string, return 0
        return 0
    return haystack.find(needle) #return -1 if the needle is not found

# Test cases
print(strStr("hello", "ll"))   # Output: 2 (substring 'll' starts at index 2)
print(strStr("aaaaa", "bba"))  # Output: -1  (substring 'bba' is not found )
