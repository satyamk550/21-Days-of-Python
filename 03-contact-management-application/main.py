def add_person():
    name = input("name: ")
    age = input("age: ")
    email = input("email: ")

    person = {"name": name, "age": age, "email": email}
    return person

print("hi, welcome to the contact management application")
print()

command = input("you can 'add', 'delete' or 'search' for a contact: ").lower()

# Changed variable name from 'person' to 'people' to avoid overwriting conflicts
people = []

if command == "add":
    new_person = add_person()   # Capture the returned dictionary
    people.append(new_person)   # Append it to our list
    print("contact added successfully")
    print("Current contacts:", people)  # Optional: to verify it was added
elif command == "delete":
    pass
elif command == "search":
    pass
else:
    print("invalid command")