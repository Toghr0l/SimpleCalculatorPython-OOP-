from colorama import Fore

def DoYouWantToC(hasEnteredOption):
    option = input("Do you want to run it again? (y or n): ").lower()
    if option == "y":
        hasEnteredOption = False
    elif option == "n":
        print(Fore.BLUE + "Thanks for using!" + Fore.RESET)
        print(f"{Fore.YELLOW}GitHub: https://github.com/toghr0l{Fore.RESET}")
        hasEnteredOption = True
    return hasEnteredOption