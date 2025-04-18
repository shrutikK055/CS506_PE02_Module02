# Try block to attempt getting input and performing addition

try:
    num1 = int(input("Enter first number: ")) #take user input 1 and convert it to an integer

    num2 = int(input("Enter second number: "))  #take user input 2 and convert it to an integer

    print("Sum is:", num1 + num2) #add both the integers and print the result

except ValueError: #It will print below message if there is any error converting input to an integer
    
    print("Please enter valid numbers.")


