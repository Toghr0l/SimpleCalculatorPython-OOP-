from time import sleep
import myClass 
import colorama
from colorama import Fore, Back, Style

hasEnteredOption = False   

print(f"{Fore.GREEN}This is a calculator!{Fore.RESET}")

while hasEnteredOption == False:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    
    option = input("Enter a choice among (+ - * /): ")
    if option == "+":
        myClass.Calculating()
        print(f"{Fore.YELLOW}Sum is {num1 + num2}{Fore.RESET}")
        hasEnteredOption = True
        hasEnteredOption = myClass.DoYouWantToC(hasEnteredOption)
    elif option == "-":
        myClass.Calculating() 
        print(f"{Fore.YELLOW}Minus is {num1 - num2}{Fore.RESET}")
        hasEnteredOption = True
        hasEnteredOption = myClass.DoYouWantToC(hasEnteredOption)
    elif option == "*":
        myClass.Calculating()
        print(f"{Fore.YELLOW}Multiple is {num1 * num2}{Fore.RESET}")
        hasEnteredOption = True
        hasEnteredOption = myClass.DoYouWantToC(hasEnteredOption)
    elif option == "/":
        myClass.Calculating()
        print(f"{Fore.YELLOW}Devision is {num1 / num2}{Fore.RESET}")
        hasEnteredOption = True
        hasEnteredOption = myClass.DoYouWantToC(hasEnteredOption)
    else:
        print(f"{Fore.RED}Invalid input!{Fore.RESET}")
        hasEnteredOption = False
