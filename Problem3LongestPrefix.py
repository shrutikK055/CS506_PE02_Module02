# Take input from the user for the first string (space-separated list of strings)
user_input = input("Enter a list of strings separated by spaces: ")


#  Function to find the longest common prefix among a list of strings

def longestCommonPrefix(strs):
    if not strs:  # If the list is empty, return an empty string
        return ""
    prefix = strs[0]  # Start by assuming the prefix is the first string
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1] # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""
    return prefix  # Return the longest common prefix found

# Split the user input into a list of strings and call the function
str_list = user_input.split()

#print the result
print("Output:", longestCommonPrefix(str_list))
