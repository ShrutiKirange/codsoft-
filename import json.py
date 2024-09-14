import json
import re
import shutil

# Define the Contact Book class
class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def backup_contacts(self):
        try:
            shutil.copy(self.filename, f"{self.filename}.backup")
        except FileNotFoundError:
            pass

    def save_contacts(self):
        self.backup_contacts()
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        if not self.validate_phone(phone) or not self.validate_email(email):
            return
        
        self.contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def view_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {name}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        contact = self.contacts.get(name)
        if contact:
            if phone:
                if self.validate_phone(phone):
                    contact['Phone'] = phone
            if email:
                if self.validate_email(email):
                    contact['Email'] = email
            if address:
                contact['Address'] = address
            self.save_contacts()
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        if self.contacts:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
        else:
            print("No contacts available.")

    def search_contacts(self, query):
        results = {name: details for name, details in self.contacts.items() if query.lower() in name.lower() or query in details.values()}
        if results:
            for name, details in results.items():
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
        else:
            print(f"No contacts found matching '{query}'.")

    @staticmethod
    def validate_phone(phone):
        if re.fullmatch(r"\+?\d[\d\s\-()]*", phone):
            return True
        print("Invalid phone number format.")
        return False

    @staticmethod
    def validate_email(email):
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        print("Invalid email address format.")
        return False

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Search Contacts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter home address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            name = input("Enter name of the contact to view: ")
            contact_book.view_contact(name)
        elif choice == '3':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (or leave blank to keep current): ")
            email = input("Enter new email address (or leave blank to keep current): ")
            address = input("Enter new home address (or leave blank to keep current): ")
            contact_book.update_contact(name, phone or None, email or None, address or None)
        elif choice == '4':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            contact_book.list_contacts()
        elif choice == '6':
            query = input("Enter name, phone, or email to search: ")
            contact_book.search_contacts(query)
        elif choice == '7':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()