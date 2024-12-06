# Main module containing main menu, user interaction, and error handling
import book_menu as b_m
import user_menu as u_m
import author_menu as a_m

def main():
    print("Library Management System with Database Integration")
    while True:
        try:
            print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
            user_input = input("Enter your choice: ").strip()
            if user_input == '1':
                b_m.display_book_menu()
            elif user_input == '2':
                u_m.display_user_menu()
            elif user_input == '3':
                a_m.display_author_menu()
            elif user_input == '4':
                print("Quitting the system...")
                break
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()