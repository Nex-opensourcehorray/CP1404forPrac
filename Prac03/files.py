"""
CP1404/CP5632 - Practical
The intention here is to give you experience using different ways
to read files and answer the following questions.
"""

# 1, ask name for file with open and close.
user_name = input("Please input your name:")
in_file = open("name.txt", 'w')
print(user_name, file=in_file)
in_file.close()

# 2, print your name from file with open and close.
out_file = open("name.txt", 'r')
for line in out_file:
    print(f"Hello! {line}")
out_file.close()

# 3, grab your first-two text number from file with calculation.
with open("numbers.txt", 'r') as out_file:
    line0 = out_file.readline().strip()
    text = int(line0)
    line1 = out_file.readline().strip()
    text1 = int(line1)
    total_num = text + text1
    print(total_num)
    print(end='\n')


# 4, grab your text number from file with full printing.
with open("numbers.txt", 'r') as out_file:
    for line in out_file:
        print(line.strip())
