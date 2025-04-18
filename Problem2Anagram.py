# Take input from the user for the first string
s = input("Enter the first string (s): ")

# Take input from the user for the second string
t = input("Enter the second string (t): ")


# Function to check if two strings are anagrams
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# print the result
print("Are the two strings anagrams?", isAnagram(s, t))