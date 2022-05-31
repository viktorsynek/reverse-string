import time

def another():
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()

def reverse_string(word):
    lst = []
    for i in word:
        lst.append(i)
    lst.reverse()
    result = ""
    for x in lst:
        result += x
    time.sleep(1)
    print("Reversed:", result) 

def start():
    print("Give me a word, I'll reverse it: ")
    time.sleep(1)
    word = input("Input: ")
    reverse_string(word)
    time.sleep(1)
    another()

start()
