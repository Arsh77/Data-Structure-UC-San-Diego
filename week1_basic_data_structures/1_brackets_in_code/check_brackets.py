# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next1 in enumerate(text):
        if next1 in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next1,i])
        if next1 in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)>0:
                if not are_matching(opening_brackets_stack.pop()[0],next1):
                    return i+1
            else:
                return i+1
                
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack.pop()[1]+1
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    while True:
        main()
