"""
we have to create a dictionary, similar to the real-world dictionary.

The details and functionalities that are essential and must be present are:

User will give a word as an input. Suppose that the word is present in your dictionary along with its definition or meaning.
The program will print the meaning or definition of that word.
For example:
The user inputs the word : “programming”

The output will be:

 "the process of writing computer programs"
The above one was just an example.
One word outputs are preferred.
"""

dic = {"Anger": "Rage", "Aid": "Help", "Attack": "Assault", "Clean": "Neat"}

k = input("Enter the word which you want to know the meaning of\n")


try:
    print(dic[k])
except Exception as e:
    print("Sorry! The word was not found in our dictionary.")