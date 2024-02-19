############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import time

def another():
    # IF USER INPUTS "N" THE PROGRAM STOPS
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()

def start():
    print("Give me a word, I'll reverse it: ")
    time.sleep(1)
    # THE USER GIVES THE WORD THEY WANT TO GET REVERSED
    word = input("Input: ")
    reverse_string(word)
    time.sleep(1)
    another()

def reverse_string(word):
    result = ""
    # LOOPS THROUGH THE WORD
    # FROM THE LAST CHARACTER TILL THE FIRST ONE
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    time.sleep(1)
    print("Reversed:", result)

start()
