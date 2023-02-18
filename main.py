# python3
# Ēriks Lijurovs, RDBD0 16.grupa, 221RDB041

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    print(left, right)
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            else:
                opening_brackets_stack.pop()

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[-1].position + 1

def main():
    choice = input()
    if choice == 'F':
        test = input()
        with open('test/' + test) as file:
            text = file.read().replace("\n", "")
        file.close()
    elif choice == 'I':
        text = input()
    else:
        print("Please input F or I")
        return

    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
