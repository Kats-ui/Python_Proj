donations = []

def log_donation():
    print("\n--- Log a Donation ---")
    name = input("Enter donor's name: ")
    try:
        amount = float(input("Enter donation amount: $"))
        if amount <= 0:
            print("Donation must be a positive number!")
            return
    except ValueError:
        print("Invalid input! Please enter a number")
        return

    donations.append({"name": name, "amount": amount})
    print(f"Thank you, {name}, for donating ${amount:.2f}!")

def view_donation():
    print("\n--- All Donations ---")
    if not donations:
        print("No donations yet!")
        return

    total_amount = 0
    for i, d in enumerate(donations, start=1):
        print(f"{i}. {d['name']} donated ${d['amount']:.2f}")
        total_amount += d['amount']

    print(f"Total Donations Collected: ${total_amount:.2f}")

def donor_summary():
    print("\n--- Donor Summary ---")
    donor_name = input("Enter donor's name: ")
    donor_donations = [d['amount'] for d in donations if d['name'].lower() == donor_name.lower()]

    if donor_donations:
        total = sum(donor_donations)
        print(f"{donor_name} has donated ${total:.2f} across {len(donor_donations)} donations.")
    else:
        print(f"No donations found for {donor_name}.")

def main():
    while True:
        print("\n--- Charity Donation Tracker Menu ---")
        print("1. Log a donation")
        print("2. View all donations")
        print("3. Donor summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            log_donation()
        elif choice == "2":
            view_donation()
        elif choice == "3":
            donor_summary()
        elif choice == "4":
            print("Thank you for supporting charity! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
