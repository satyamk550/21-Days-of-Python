import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACT_FILE = os.path.join(BASE_DIR, "contact.json")


def add_person():
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email: ").strip()

    return {
        "name": name,
        "age": age,
        "email": email
    }


def delete_person(people):
    if not people:
        print("No contacts available to delete.")
        return

    for i, person in enumerate(people):
        print(
            f"{i + 1}. {person['name']} - "
            f"{person['age']} - {person['email']}"
        )

    while True:
        try:
            number = int(input("Enter contact number to delete: "))

            if 1 <= number <= len(people):
                break

            print("Invalid number. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

    deleted_person = people.pop(number - 1)
    print(f"{deleted_person['name']} deleted successfully.")


def search_person(people):
    if not people:
        print("No contacts available to search.")
        return

    search_name = input("Enter name to search: ").strip().lower()

    found_contacts = [
        person for person in people
        if person["name"].lower() == search_name
    ]

    if found_contacts:
        print("\nFound contacts:")

        for person in found_contacts:
            print(
                f"{person['name']} - "
                f"{person['age']} - {person['email']}"
            )
    else:
        print("No contacts found with that name.")


def save_contacts(people):
    try:
        with open(CONTACT_FILE, "w", encoding="utf-8") as f:
            json.dump({"contacts": people}, f, indent=4)
            f.write("\n")
    except OSError as error:
        print(f"Could not save contacts to {CONTACT_FILE}: {error}")
        return False

    print(f"Contacts saved to: {CONTACT_FILE}")
    return True


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        try:
            with open(CONTACT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

                if isinstance(data, dict):
                    contacts = data.get("contacts", [])
                    return contacts if isinstance(contacts, list) else []

                return []

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read contact.json.")
            return []

    return []


print("Hi, welcome to the Contact Management Application!")

people = load_contacts()

while True:
    print("\nCurrent contacts:", people)

    command = input(
        "\nChoose 'add', 'delete', 'search', or 'exit': "
    ).strip().lower()

    if command == "add":
        new_person = add_person()
        people.append(new_person)
        save_contacts(people)
        print("Contact added successfully.")

    elif command == "delete":
        old_count = len(people)
        delete_person(people)

        if len(people) < old_count:
            save_contacts(people)

    elif command == "search":
        search_person(people)

    elif command == "exit":
        save_contacts(people)
        print("Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")
