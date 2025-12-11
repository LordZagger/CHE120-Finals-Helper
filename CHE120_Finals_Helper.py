def number_triangle(): #made in collaboration with a friend at UCarleton
    while True:
        value = input("Enter An Integer Between 1 and 9: ")

        if value.isdigit() and 1 <= int(value) <= 9:
            i = int(value)

            for row in range(1, i+1):

                for col in range(row):
                    print(str(row), end= "")
    
                print()
            break

#dictionary of terms made here. key is the term, value is its definition
CHE120_dictionary = {"int": "integer", "float": "decimal number", "complex": "complex number", "concatenation": "adding strings together", "escape character": "\\, used to display otherwise undisplayable characters like ' and \" inside a string, or to make tabs or newlines (\\t, \\n)", \
                     "boolean operators": "There are 3: and, or, not. For 'and', if even one condition is False, the output will be False; for 'or', if even one condition is True, the output is True; 'not' outputs the opposite boolean value", "relational operators": "<, >, <=, >=, ==, !=; compare different values to produce a boolean value", "binary operator": "used between 2 objects", "unary operator": "used with one object", \
                     "lexicographic ordering": "strings are ordered alphabetically", "import": "imports a module", "import *": "imports everything from a module (NOT RECOMMENDED)", "__name__": "__name__ is assigned __main__ if the code is the main program; code under 'if __name__ == \"__main__\"' will therefore only run if it's the main program. If it's not the main program (aka if it was imported as a module), __name__ is assigned the name of the module.", \
                     "method": "a function specific to a class. can be called implicitly (from the object, ex: [1,2,3].count(1)), or explicitly (from the type, ex: list.count([1,2,3],1))", "index": "position of an object inside a collection. indices go from 0 to len(collection)-1, or -len(collection) to -1", \
                     "for loop": "useful when you know how many iterations you want or when you want to look at each item in a collection", "while loop": "useful when needing to do a task repeatedly while or until a condition is met", "mutability": "a collection is mutable if its entries can be updated (ex: any entry in a list can be replaced, but entries in a tuple can't)", \
                     "str (string)": "immutable, ordered collection of text", "list": "mutable, ordered collection", "tuple": "immutable, ordered collection", "set": "mutable, unordered collection that doesn't care about order and doesn't keep duplicates", "dictionary": "mutable, unordered collection that maps immutable objects (keys) to values", \
                     "slice": "portion of a collection (ex: [1,2,3][1:] will return a sublist of [1,2,3] containing the item at index 1 onwards ([2,3])", "np.ndarray (array)": "numpy's version of a matrix", "broadcasting": "arrays can be used together arithmetically if the last n digits of their shape match, where n is the dimension of the smaller array (ex: arrays of shape (2,3,2,1) and (3,2,1) can be broadcast since their last 3 digits match)", \
                     "no copy": "if A is an array, then b=A makes b refer to the same array as A, thus modifying b or A changes the array", "view/shallow copy": "a view can have its own shape but changing its entries also changes the corresponding entries of the array - use ipython to check if a method affects both the view and the original. Methods like ravel, transpose and flatten return views", \
                     "deep copy": "F=A.copy(); F is a new, distinct array with the same values as A; changing F does not change A", "np.save": "saves an array as .npy", "np.savez": "saves multiple arrays as .npz", "np.savetxt": "saves an array to a readable format you can specify", "np.load/np.loadtxt": "loads the array; use the function with its corresponding save function!", \
                     "png": "png are the ideal image format for rescaling", "pdf": "Pendar endorses pdfs as the best way to share a document as they preserve its formatting"}

CHE120_functions = ["print - display variables and text", "input - collect a typed response from a user", \
                    "min - returns the minimum value of a collection", "max - returns the maximum value of a collection", "sum - calculates and returns the sum of a collection", \
                    "len - returns the length of a collection", "type - use to check if the type of an argument is valid (ex: type(alist) != list)", \
                    "str.isalpha - use to check if a string is only alphatical characters", "range - use with for loops (ex: for i in range(3))", \
                    "np.ndarray.shape - returns the shape of the array", "np.ndarray.ndim - returns the dimension of the array", \
                    "time.perf_counter - use to calculate the time it takes for a program to run by calling this function before and after and taking the difference", "list.pop - for lists, removes and returns the item at the provided index", "list.append - adds the item to the end of the list", \
                    "np.arange - use to create a 1D array from a range, and can be reshaped as you wish", "np.ndarray.size - returns the amount of entries in an array", \
                    "np.ndarray.flatten - returns a 1D copy of the array", "np.linalg.det - returns the determinant of an array", "np.linalg.inv - returns the inverse of an array", "np.linalg.solve - returns the solution to Ax=b if A and b's sizes match properly", \
                    "plt.plot - use along with other functions like plt.xlabel, plt.ylabel, plt.xlim, plt.ylim, plt.title and plt.legend to make graphs"]

#welcome the student
print("Welcome to the CHE120 Drop-In Help Session Assistant!")
print("My programmer was about to make a powerpoint, but decided a .py file was more... creative.")
print("Please note that np stands for numpy and plt stands for matplotlib.pyplot. If using Anaconda Prompt, a word may get cut midway due to the length of the sentences (my apologies), and with Spyder, make the ipython console as big as possible so the text doesn't seem too compact.")
print()

#ask if they want to see dictionary
print("A) Would you like to read the course dictionary, which offers short descriptions of a plethora of terms from throughout the second-half of the course?")
option1 = ''
while option1 not in ['y', 'n', 'Y', 'N']: #make sure the user doesn't try putting invalid input
    option1 = input("(y for yes, n for no): ")
    if option1 not in ['y', 'n', 'Y', 'N']:
        print("Please try again with a valid input.")

if option1 in ['y', 'Y']: #lowercase or uppercase y accepted as valid options
    #print dictionary if yes
    print()
    for key in CHE120_dictionary:
        print(f"{key}: {CHE120_dictionary[key]}")
    print("(Read the lecture notes again if you feel you need to review one of the terms or how to use it!)")
    print("-"*30)
        
#ask if they want to see useful functions
print() #newline for readability
print("B) Would you like to see a list of some possibly useful functions and methods?")
option4 = ''
while option4 not in ['y', 'n', 'Y', 'N']: #make sure the user doesn't try putting invalid input
    option4 = input("(y for yes, n for no): ")
    if option4 not in ['y', 'n', 'Y', 'N']:
        print("Please try again with a valid input.")


if option4 in ['y', 'Y']: #lowercase or uppercase y accepted as valid options
    #print dictionary if yes
    print()
    for item in CHE120_functions:
        print(item)
    print("-"*30)


#ask if they want to know about common mistakes+tips
print() #newline for readability
print("C) Would you like to learn about some common mistakes and coding tips?")
option2 = '' 
while option2 not in ['y', 'n', 'Y', 'N']: #make sure the user doesn't try putting invalid input
    option2 = input("(y for yes, n for no): ")
    if option2 not in ['y', 'n', 'Y', 'N']:
        print("Please try again with a valid input.")

if option2 in ['y', 'Y']:
    print()
    #print common mistakes if yes
    print("Here are some things to watch out for on the exam.")
    print("1. Overthinking the questions/Getting stuck")
    print("- For MC, test the code or try an example in ipython and see what happens! I recommending testing the code even if the answer seems obvious.")
    print("\t - Note: if nothing shows up after you called a function, it probably returned None.")
    print("- If you read a question and don't know how to start, try the first thing that comes to mind.")
    print("\t - Make an outline of how you would do the task yourself, in English. A step in English usually has a corresponding function or method in python (ex: 'make the word uppercase' is 'word.upper()' in python)")
    print("\t - Use ipython as the Internet! If you're looking for a function or a method, search it up in ipython with the help function of the object type, or the type followed by a period then tab! (ex: if looking for a method to use with a list, enter 'help(list)' and scroll until you find what you're looking for, or type 'list.' then press tab)")
    print("\t - You don't need to have the full picture figured out; start with little bits you think you might need, like variables and setting up loops and type checks, then add the rest as you go.")
    print("- If you get stuck, move on to another question! When you come back or while you work on another question, you might get a lightbulb.")
    print("- Do not panic about making your functions perfect for every single scenario a user might try.") 
    print("\t - The provided description and examples hint at the minimum your function should be able to do -- cases not shown in the examples are cases you usually don't need to worry about if your code works for the provided examples.")
    print("- If you're unsure about something, don't hesitate to ask for clarification! (proctors are not allowed to answer questions, so wait for Pendar)")
    print()
    
    print("2. Syntax errors!")
    print("Syntax errors are by far the most common mistakes in coding.")
    print("- To avoid syntax errors, DOUBLE CHECK YOUR CODE REGULARLY!")
    print("\t - Make sure variable names are consistent, you have colons and periods at the proper places, correct indentation, the proper type of bracket AND is in a pair ({}, [], ())...")
    print("- If your code isn't working and you're not sure why, plug it into Spyder!")
    print("\t - Spyder will immediately detect syntax errors, and using the debug feature can help identify any semantic errors.")
    print()
    
    print("3. Not paying close attention to the question")
    print("- Re-read the instructions/docstring carefully and make sure your code prevents a user from entering any type of invalid input.")
    print("\t - However, you don't need to overkill your type checks... unless the question wants you to.")
    print("\t\t - Ex: If the question makes you trust that an array from the user will be entirely numbers, don't bother checking each individual entry in the array to see if it's indeed a number.")
    print("\t\t (I give this specific example because type checking the entries of an array is actually more complicated than you think due to the dtypes...)")
    print("- Pay CLOSE attention to the instructions/docstring. If they want a specific type and format for the argument(s), check if each of the argument's properties match the required.")
    print("\t - Ex: If the argument must be a square 2D array, check if it's of type np.ndarray, that ndim is 2 and that shape[0]==shape[1].")
    print("\t - If checking multiple properties of an argument at the same time, I recommend checking the type first, so the code returns None before it has a chance to plug that invalid argument into a method that will result in an error")
    print("- If you need to RETURN something, make sure you RETURN. If they want you to RETURN a NEW item, and not modify the original, MAKE SURE YOU DON'T MODIFY THE ORIGINAL and RETURN A NEW OBJECT.")
    print()
    
    print("4. Forgetting to update the iterator of a while loop (i.e. forgetting i += 1)")
    print("- If you have a while loop and you notice the program doesn't stop running, it might be because you forgot to update the iterator, resulting in an infinite loop. Force stop the program and fix your cdde!")
    print("- DOUBLE CHECK YOUR CODE and make sure the iterator is being updated properly!")
    print()
    
    print("5. As Pendar has hopefully said multiple times, save your file regularly, and submit it to the dropbox every once and a while.")
    print("-"*30)

#ask if they want more resources
print() #newline for readability
print("That is all from me. As a bonus, would you like some extra practice resources? (If you're done all other practice, are getting bored and want something to try?)")
option3 = ''
while option3 not in ['y', 'n', 'Y', 'N']: #make sure the user doesn't try putting invalid input
    option3 = input("(y for yes, n for no): ")
    if option3 not in ['y', 'n', 'Y', 'N']:
        print("Please try again with a valid input.")

if option3 in ['y','Y']:
    print()
    #give extra resources if yes
    print("Here is the website Jeremy used to learn Python before 1A. It contains easy to medium difficulty coding exercises of everything except numpy.")
    print("--> https://open.cs.uwaterloo.ca/python-from-scratch/")
    print("Here is a website Jeremy found with easy to hard coding challenges. Be aware he doesn't actually know how easy or hard they can get...")
    print("--> https://www.hackerrank.com/domains/python/")
    print("Please note these questions might not be like what you see on the exam. THIS IS JUST FOR EXTRA PRACTICE.")
    print("(Please copy-paste into a browser the link(s) you wish to visit.)")

#say goodbye
print() #newline for readability
if option1 in ['n', 'N'] and option2 in ['n', 'N'] and option3 in ['n', 'N'] and option4 in ['n', 'N']:
    print("Congratulations on skipping through this code! I'm sad you don't want my help, but... oh well! Seems you're confident you know your stuff!")
    print("Here's a number triangle for you!")
    number_triangle()
print("Good luck, and believe in yourself! Show this last exam's who's the boss!")