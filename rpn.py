#!/usr/bin/env python3
import readline
from colorama import init, deinit
from colorama import Fore, Back, Style

init()

def calculate(arg):
    stack = []
    tokens = arg.split()
    
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                result = val1 / val2
            elif token == '^':
                result = val1 ** val2

            stack.append(result)
    if len(stack) > 1 :
        raise ValueError('too many arguments on the stack')
    
    
    return stack[0]



def main():
    while True:
        try:
            result = calculate(input('rpn calc> '))
            
            if result < 0:
                print(Fore.RED + str(result) + Fore.WHITE)
            elif result > 0:
                print(Fore.GREEN + str(result) + Fore.WHITE)
            else:
                print(Fore.BLUE + str(result) + Fore.WHITE)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
