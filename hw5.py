'''
1.1 What command will tell you what your working directory is?
    pwd
1.2 What command with list all the files in your current working directory?
    ls
1.3 What commands will let you move to the correct repository and pull the latest changes?
    cd ../brianna_repo
    git pull origin main
1.4 How would you move this new homework.py to your personal repository homework directory?
    cp -r homework.py  ../judy_decal/homework
1.5 You want to see the contents of the homework.py in your terminal from your personal repository. What command(s) will let you do this?
    nano homework.py or cat homework.py
1.6 You want to edit the contents of the homework.py in your terminal from your personal repository. What command will let you do this?
    nano homework.py
1.7 What commands will allow you to save the changes and push from your local repository to your remote repository?
    git add
    git commit -m
    git push origin main
1.8 What commands should you call to resolve this error and push your homework properly? What does the error mean?
    git pull origin main
    git add homework.py
    git commit -m "Adding homework"
    git push origin main
1.9 What absolute path will allow you to move to Recents/? 
    cd ../../Recents/
'''

# 2.1 Data Types - Write a function that takes any input and returns a string indicating its data type.
def checkDataType(input):
    return str(type(input))
# s.replace() and get rid of < class and > ??
print(checkDataType(3.14))
print(checkDataType(True))

# 2.2 Conditionals - Write a function that takes any input and returns a string indicating its data type.
def evenOrOdd(value):
    if value % 2 == 1:
        return "Odd"
    if value % 2 == 0:
        return "Even"
print(evenOrOdd(7))
print(evenOrOdd(10))

# 3 Loops - Write a function that takes a list of integers and returns their sum using a loop
def sumWithLoop(numbers):
    sum = 0 
    for x in numbers:
        sum += x
    return sum
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# 4.1 Lists - Write a function that takes a list and returns a new list with each element duplicated.
def duplicateList(list):
    duplicates = []
    for x in list:
        duplicates.append(x)
        duplicates.append(x)
    return duplicates
list = ['a', 'b', 'c']
print(duplicateList(list))

# 4.2 Debugging - There’s an error in the following function that’s supposed to return the square of a number. Find and correct it:
def square(num): # missing : added 
    return num * num
