"""
CP1404/CP5632 - Practical
The List review with more questions need to be answering and more List coding.
"""
# 1. Basic list operations (List usage rewind)
Numbers = [6, 14, 9, 3, 21]
for number in Numbers:
    print(f"Number: {number}")
print(f"The first number is: {Numbers[0]}")
print(f"The last number is: {Numbers[-1]}")
print(f"The smallest number is: {min(Numbers)}")
print(f"The largest number is: {max(Numbers)}")
print(f"The average of the numbers is: {sum(Numbers)/len(Numbers)}")

# 2. Woefully inadequate security checker (List with conditional statement)
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("Plz input your username:")
if user_name in usernames:
    print("Access Granted!")
else:
    print("Access Denied!")