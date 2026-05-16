# Simple customer management tool: query, add, delete records via CLI.
customer_records = {
    "Lilian": {"email": "lilian6@hotmail.com", "date": "1.1.2020"},
    "Jack":   {"email": "jackw@hotmail.com",   "date": "5.2.2024"},
    "Oliver": {"email": "oliverz@hotmail.com", "date": "5.12.2016"},
}

while True:
    action = input("\nChoose an action: 1.Query  2.Add  3.Delete  4.Exit\n").strip()

    if action == "1":
        name = input("Enter name: ").strip()
        if name in customer_records:
            print(f"{name}: {customer_records[name]}")
        else:
            print("Customer not found.")

    elif action == "2":
        name = input("Name: ").strip()
        if name in customer_records:
            print("This customer already exists.")
            continue
        email = input("Email: ").strip()
        date  = input("Join date: ").strip()
        customer_records[name] = {"email": email, "date": date}
        print(f"{name} added successfully.")

    elif action == "3":
        name = input("Enter the name to delete: ").strip()
        if customer_records.pop(name, None):
            print(f"{name} has been deleted.")
        else:
            print("Customer not found.")

    elif action == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter 1-4.")