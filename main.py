from src.utils.student_manager import StudentManager

def main_menu():
    manager = StudentManager()

    while True:
        print("\n--- Student Manager Menu ---")
        print("1. Create new student list")
        print("2. Add student to list")
        print("3. Sort students alphabetically (in all lists)")
        print("4. Search student in list")
        print("5. Show all students")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_list()
            print("New student list created.")

        elif choice == "2":
            if not manager.students:
                print("No student lists found. Please create a list first.")
                continue
            try:
                list_id = int(input("Enter list ID: "))
                name = input("Enter student name and surname: ")
                manager.add(list_id, name)
                print(f"Student '{name}' added to list {list_id}.")
            except (IndexError, ValueError):
                print("Invalid list ID.")

        elif choice == "3":
            manager.sort_students_alphabetically()

        elif choice == "4":
            if not manager.students:
                print("No student lists available.")
                continue
            try:
                list_id = int(input("Enter list ID: "))
                name = input("Enter student name to search: ")
                found = manager.search(list_id, name)
                print("Found!" if found else "Not found.")
            except (IndexError, ValueError):
                print("Invalid list ID.")

        elif choice == "5":
            for idx, lst in enumerate(manager.students):
                print(f"List {idx}: {lst}")

        elif choice == "0":
            print("Exiting Student Manager. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
