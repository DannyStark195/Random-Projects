#Day0
import os

class Contact():
    DELIMETER = "|"
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def __str__(self):
        return f"{self.name}{self.DELIMETER}{self.number}"

class ContactsManager():
    # Create a contact book if it doesn't exist
    def create_contact_book(self, contact_book):
        self.contact_book = contact_book
        if not os.path.exists(contact_book):
            with open(contact_book, 'w') as contact_book:
                pass

    # Reads a contact book if it does exist, else it creates it
    def read_contact_book(self, contact_book):
        self.contact_book = contact_book
        if os.path.exists(self.contact_book):
            with open(self.contact_book, 'r') as contact_book_open:
                open_contact_book = contact_book_open.read()
                if not open_contact_book.strip():
                    print(f"{self.contact_book} is empty")  # prints contact book is empty if there is nothing in it.
                else:
                    print(open_contact_book)
        else:
            self.create_contact_book(self.contact_book)
            print(f"{self.contact_book} created successfully")
    
    # Add contacts to contact book
    def add_contact(self):
        while True:
            # check if contact name is valid
            contact_name = input("Enter Contact name: ")
            if not contact_name.strip():
                print("Contact name cannot be empty")
                continue
            # check if contact phone number is valid
            phone_number = input("Enter Contact phone number: ")
            if not phone_number.strip() or not phone_number.isdigit():
                print("invalid Phone number! Phone number must be a number")
                continue
            
            with open(self.contact_book, 'r+') as contact_book_open:
                open_contact_book = contact_book_open.readlines()
                # check if name or number already exists in contact book
                if any(contact_name in line for line in open_contact_book):
                    print(f"{contact_name} already exists, please add a different name")
                    continue                      
                if any(phone_number in line for line in open_contact_book):
                    print(f"{phone_number} already exists with this contact, please add a different phone number")
                    continue    
                else:
                    new_contact = Contact(contact_name, phone_number)
                    add_new_contact = str(new_contact) + '\n'
                    contact_book_open.write(add_new_contact)
                    print("Contact added successfuly!")
                    break

    # Search for a contact in contact book
    def search_contact(self):
        while True:
            contact_to_search = input("Enter name or phone number you wish to search: ")
            with open(self.contact_book, 'r') as contact_book_open:
                found = False
                for line in contact_book_open:
                    if not line.strip():
                        continue  # if contact book is empty, do nothing
                    name, *numbers = line.strip().split('|')  # split each line to name | numbers
                    # Search if name or number in line
                    if contact_to_search in name or contact_to_search in numbers:
                        print(line.strip())
                        found = True
                        return name
                if not found:
                    print(f"'{contact_to_search}' not found in contact book.")
                    break 

    # Add a number to a contact
    def add_number(self):
        contact_to_add_number = self.search_contact()  # check if contact exist in contact book using the search_contact method
        if contact_to_add_number:
            while True:
                phone_number = input("Enter Contact phone number: ")
                if not phone_number.strip() or not phone_number.isdigit():
                    print("invalid Phone number! Phone number must be a number")
                    continue
                
                with open(self.contact_book, 'r') as contact_book_open:
                    open_contact_book = contact_book_open.readlines()
                    if any(phone_number in line for line in open_contact_book):
                        print(f"{phone_number} already exists with this contact, please add a different phone number")
                        continue            
                    else:
                        for i, line in enumerate(open_contact_book):
                            name, *numbers = line.strip().split('|')
                            # if number is not in contact book, edit the line that has the contact and add number
                            if name == contact_to_add_number:
                                open_contact_book[i] = line.strip() + "|" + phone_number + "\n"
                                break
                with open(self.contact_book, 'w') as contact_book_open:
                    contact_book_open.writelines(open_contact_book)  # write the new lines with the number added
                    print("Phone number added successfully!!!")
                    break

    # update/edit contact name
    def update_contact_name(self):
        contact_name_edit = self.search_contact()  # searches for the name and returns it into contact_name_found if found
        if contact_name_edit:
            while True:
                updated_name = input("Enter new contact name: ")
                if not updated_name.strip():
                    print("Contact name cannot be empty")
                    continue
                # verify the updated_name
                with open(self.contact_book, 'r') as contact_book_open:
                    open_contact_book = contact_book_open.readlines()
                    if any(updated_name in line for line in open_contact_book):
                        print(f"{updated_name} already exists, please add a different name")
                        continue
                    # check if new name exists           
                    else:
                        for i, line in enumerate(open_contact_book):
                            name, *numbers = line.strip().split('|')
                            # if updated_name is not in contact book, edit the line that has the name and update the name
                            if name == contact_name_edit:
                                open_contact_book[i] = updated_name + "|" + "|".join(numbers) + "\n"
                                break
                with open(self.contact_book, 'w') as contact_book_open:
                    contact_book_open.writelines(open_contact_book)  # writes the new lines with the updated name
                    print("Contact updated successfully!!!")
                    break

    # Update/edit contact number
    def update_contact_number(self):
        while True:
            number_to_edit = input("Enter the phone number you wish to edit: ")
            updated_phone_number = input("Enter new phone number: ")
            if not updated_phone_number.strip() or not updated_phone_number.isdigit():
                print("Invalid Phone number! Phone number must be a number")
                continue  # validate number
            with open(self.contact_book, 'r') as contact_book_open:
                open_contact_book = contact_book_open.readlines()
                if any(updated_phone_number in line for line in open_contact_book):
                    print(f"{updated_phone_number} already exists, please add a different number")
                    continue  # check if the new number exists
                else:
                    found = False
                    for i, line in enumerate(open_contact_book):
                        name, *numbers = line.strip().split('|')
                        # if number_to_search is in the numbers in that line 
                        if number_to_edit in numbers:
                            numbers = [updated_phone_number if number == number_to_edit else number for number in numbers]  # for the numbers in that line changes the number to the new number, else keeps the same number
                            open_contact_book[i] = name + "|" + "|".join(numbers) + "\n"
                            found = True
                            break
                    if not found:
                        print(f"'{number_to_edit}' not found")
                    if found:
                        print("Contact phone number updated successfully!!!")
            with open(self.contact_book, 'w') as contact_book_open:
                contact_book_open.writelines(open_contact_book)  # writes the new lines with the updated number
                break

    def delete_contact_number(self):
        number_to_delete = input("Enter the phone number you wish to delete: ")
        with open(self.contact_book, 'r') as contact_book_open:
            open_contact_book = contact_book_open.readlines()
            found = False
            for i, line in enumerate(open_contact_book):
                name, *numbers = line.strip().split('|')  # splits the line to name|numbers
                if number_to_delete in numbers:
                    numbers.remove(number_to_delete)  # removes the number_to_delete from the numbers in the line that has the number
                    open_contact_book[i] = name + "|" + "|".join(numbers) + "\n"
                    found = True
                    break
            if not found:
                print(f"'{number_to_delete}' not found")
            if found:
                print("Contact phone number deleted successfully!!!")
        with open(self.contact_book, 'w') as contact_book_open:
            contact_book_open.writelines(open_contact_book)  # writes the new lines

    def delete_contact(self):
        contact_to_delete = input("Enter the contact name or phone number you wish to delete: ")
        with open(self.contact_book, 'r') as contact_book_open:
            open_contact_book = contact_book_open.readlines()
            found = False
            for i, line in enumerate(open_contact_book):
                name, *numbers = line.strip().split('|')
                if contact_to_delete == name or contact_to_delete in numbers:
                    open_contact_book[i] = ""  # remove that line completely    
                    found = True
            if not found:
                print(f"'{contact_to_delete}' not found in contact book.")
            if found:
                print("Contact deleted successfully!!!")
        with open(self.contact_book, 'w') as contact_book_open:
            contact_book_open.writelines(open_contact_book)  # writes the new lines wihout the contact_to_delete

# Main function
def main():
    c_manager = ContactsManager()
    while True:
        print("              CONTACTS MANAGER APP          ")       
        userchoice0 = input(""" 1. Create new Contact book  
   2. Read an existing one:  
    """)
        if userchoice0 == '1' or userchoice0 == '2':
            contact_book = input('Enter name of contact book: ')
            contact_book = contact_book + ".txt"
            c_manager.read_contact_book(contact_book)
            break
        else:
            print("Invalid input")
            continue
    while True:
        userchoice1 = input("""       a. View all contacts 
        b. Add new contact
          c. Search for a contact
            d. Update contact book
              e. Delete from contact book
                q. Quit() 
                  """)
        if userchoice1 == 'a':
            c_manager.read_contact_book(contact_book)
        elif userchoice1 == 'b':
            c_manager.add_contact()
        elif userchoice1 == 'c':
            c_manager.search_contact()
        elif userchoice1 == 'd':
            userchoice3 = input(""" 1. Add phone number to a contact 
            2. Edit the name of a contact
               3. Edit a number of a contact  """)
            if userchoice3 == '1':
                c_manager.add_number()
            elif userchoice3 == '2':
                c_manager.update_contact_name()
            elif userchoice3 == '3':
                c_manager.update_contact_number()
            else:
                print("invalid input")
        elif userchoice1 == 'e':
            userchoice3 = input(""" 1. Delete phone number from a contact 
             2. Delete contact completely   """)
            if userchoice3 == '1':
                c_manager.delete_contact_number()
            elif userchoice3 == '2':
                c_manager.delete_contact()
            else:
                print("Invalid choice")
        elif userchoice1 == 'q':
            print("Closing Contact book.........")
            print("Contact book closed...")
            break
        else:
            print("invalid input")
            continue

if __name__ == "__main__":
    main()

# Created By Danny Stark
# Took 8 days
#created on 16/05/2025