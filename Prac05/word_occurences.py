"""
CP1404/CP5632 Practical
User strings with dictionary printing.
Instruction time: 8:32 p.m.
Complete time: 9:17 p.m.
Estimate time: 40 minutes
Actual time: 45 minutes
"""
word_occurrences = {}


def main():
    """This function is to fetch user input and get the key information."""
    user_input = input("Your text:").lower()
    glossarys = user_input.split()  # by this time I need to confirm the splitting context it is match.

    for glossary in glossarys:
        if glossary in word_occurrences:
            word_occurrences[glossary] += 1
        else:
            word_occurrences[glossary] = 1

    list(word_occurrences.keys()).sort()
    key_length = max(len(key) for key in word_occurrences.keys())
    """use comprehension to get the key max length."""
    for word in word_occurrences:
        print(f"{word: <{key_length}}:{word_occurrences[word]}")


if __name__ == '__main__':
    main()