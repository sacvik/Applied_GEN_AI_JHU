import os
from src.secure_password_manager import SecurePasswordManager

from colorama import init, Fore, Style

def print_logo():
    init()  # Initialize colorama
    logo = f"""
    {Fore.GREEN}╔═══════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║  🔐 VAULT KEEPER: SECURE ACCESS       ║{Style.RESET_ALL}
    {Fore.GREEN}╠═══════════════════════════════════════╣{Style.RESET_ALL}
    """
    print(logo)


def main_menu():
    # Clear screen and print logo
    os.system('cls' if os.name == 'nt' else 'clear')
    print_logo()
    
    pm = SecurePasswordManager()
    
    while True:
        print("\n--- Secure Password Manager ---")
        if not pm.current_user:
            print("1. Login")
            print("2. Signup")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                pm.login()
            elif choice == '2':
                pm.signup()
            elif choice == '3':
                print("Thank you for using Secure Password Manager. Goodbye!")
                break
        else:
            print("\n1. Add Password")
            print("2. View Passwords")
            print("3. Search Passwords")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                pm.add_password()
            elif choice == '2':
                pm.view_passwords()
            elif choice == '3':
                pm.advanced_search()
            elif choice == '4':
                pm.logout()

if __name__ == "__main__":
    main_menu()
