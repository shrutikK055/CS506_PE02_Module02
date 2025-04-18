#count words function
def count_words_in_file():
    #input name of the file

    filename = input("Enter the name of the text file to count words: ")
    try:
        # Try to open the file

        with open(filename, 'r') as file:

            # Read the file
            text = file.read()

            # Split the text
            words = text.split()

            # Print the number of words found in the file
            print("Number of words in", filename + ":", len(words))

    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        print("File", filename, "not found.\n")

#defining function
def guest_book():
    print("\n--- Guest Book ---")
    while True:
        # Prompt the user
        name = input("Enter your name (or type 'q' to quit): ")

        # Check if the user wants to quit
        if name.lower() == 'q':
            break

        # Greet the user
        print("Hello,", name + "!")

        # Append the name
        with open("guest_book.txt", 'a') as file:
            file.write(name + "\n")

# defining function

def read_pet_files():

    # Loop through a list of pet file names
    for filename in ["cats.txt", "dogs.txt"]:
        try:

            # Try to open the file in read mode
            with open(filename, 'r') as file:

                # Print the contents
                print("\nContents of", filename + ":")

                print(file.read())

        except FileNotFoundError:
            # Handle the case when the file doesn't exist
            print("Sorry, the file", filename, "was not found.")

# Run all functions
if __name__ == "__main__":
    
    count_words_in_file()  # Run the word count function
    guest_book()           # Run the guest book function
    read_pet_files()       # Run the pet file reader function
