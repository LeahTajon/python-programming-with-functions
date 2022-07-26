"""
File: fruit.py
Author: Leah Tajon

Assignment:
Write a small Python program named fruit.py that demonstrate object
oriented programming by modifying a list. 
"""

# 01 | Open a new blank file in VS Code and save it as fruit.py
# 02 | Copy and paste this code at the top of your fruit program.
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # 03 | Add code to reverse and print fruit_list
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")

    # 04 | Add code to append "orange" to the end of fruit_list
    #      print the list.
    fruit_list.append("orange")
    print(f"Append Orange: {fruit_list}")

    # 05 | Add code to find where "apple" is located in fruit_list
    #      and insert "cherry" before "apple" in the list and print the list.
    #print(f"Index Apple: {fruit_list.index('apple')}")
    fruit_list.insert(1, "cherry")
    print(f"Insert Cherry: {fruit_list}")

    # 06 | Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"Remove Banana: {fruit_list}")

    # 07 | Add code to pop the last element from fruit_list and
    #      print the popped element and the list.
    fruit_list.pop()
    print(f"Pop Orange: {fruit_list}")

    # 08 | Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    # 09 | Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f"Clear: {fruit_list}")

main()