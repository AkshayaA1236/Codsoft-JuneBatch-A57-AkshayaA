
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[phone] = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts.values():
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts.values() if search_term in contact['name'] or search_term in contact['phone']]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                self.display_contact(contact)

    def update_contact(self, phone):
        if phone in self.contacts:
            print("Enter new details (leave blank to keep current):")
            name = input(f"Name ({self.contacts[phone]['name']}): ") or self.contacts[phone]['name']
            email = input(f"Email ({self.contacts[phone]['email']}): ") or self.contacts[phone]['email']
            address = input(f"Address ({self.contacts[phone]['address']}): ") or self.contacts[phone]['address']
            self.contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def display_contact(self, contact):
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    def user_interface(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                search_term = input("Enter name or phone number to search: ")
                self.search_contact(search_term)
            elif choice == '4':
                phone = input("Enter the phone number of the contact to update: ")
                self.update_contact(phone)
            elif choice == '5':
                phone = input("Enter the phone number of the contact to delete: ")
                self.delete_contact(phone)
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Start the Contact Book application
contact_book = ContactBook()
contact_book.user_interface()
