# LoveLocal-assignment-easy1
Given a string s consisting of words and spaces, return the length of the last word in the string.

Explanation of Code:

Step 1 -> Function Definition: Defining a function named length_of_lastword that takes a string s as input, splits it into words using split(), and returns the length of the last word. If there are no words, it returns 0.

Step 2 -> User Input: Prompts the user to input a string. The entered string is stored in the variable s.

Step 3 -> Function Call and Result Assignment: Calls the length_of_lastword function with the user-inputted string s. The result is assigned to the variable result.

Step 4 ->P rinting Result: Prints the result obtained from the function call.

When you run this program in Python IDLE:

It will prompt you to enter a string.

After entering the string, the function length_of_lastword will be called with the inputted string.

The result, which is the length of the last word (or 0 if there are no words), will be stored in the variable result.

Finally, the program will print the result.

Example 1:

Input: s = "Hello World"

Output: 5

Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "

Output: 4

Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"

Output: 6

Explanation: The last word is "joyboy" with length 6.

