#defining a function named 'length_of_lastword ' that takes single parameter 's' (apparantly a string)
def length_of_lastword(s):
    # Split the input string 'str' into  list of words
    words = s.split()

    # Check if there are any words
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

#taking user input
s=input("Enter a String:")

#fuction call
result= length_of_lastword(s)

#printing the result
print(result)


