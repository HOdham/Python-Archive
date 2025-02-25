#in modify first an last name reveresd otherwise really nice job
#39/40



import hmenu
import os
#Hendrix Odham 
#this code is not my best work its kinda messy
def formatPnumber(phone_number):
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"


def createContact(firstName, lastName, phoneNumber, *args):
    formattedFirstName = firstName.title()
    formattedLastName = lastName.title()

    formattedArgs = ""
    for arg in args:
        if arg:
            formattedArgs += f",{arg}"
        else:
            formattedArgs += ",None"

    csvString = f"{formattedLastName},{formattedFirstName},{phoneNumber}{formattedArgs}\n"
    return csvString

def saveContact(contactCSV, filename):
    try:
        file = open(filename, "a")
        file.write(contactCSV)
        print("CONTACT WAS SAVED")
    except Exception as e:
        print(f"Error saving contact: {e}")
    finally:
        file.close()

def displayAll(filename):
    try:
        file = open(filename, "r")
        for line in file:
            printPerson(line)
    except FileNotFoundError:
        print("Contacts file not found.")
    except Exception as e:
        print(f"Error displaying contacts: {e}")
    finally:
        file.close()

def printPerson(contactCSV):
    fields = contactCSV.strip().split(',')
    phonenummber = formatPnumber(fields[2])
    lastName = fields[0].title()
    firstName = fields[1].title()
    print(f"{lastName} - {firstName}")
    print(f"{phonenummber}")
    for field in fields[3:]:
        if field != 'None':
            print(field)
    print()

def searchContacts(firstName, lastName, filename):
    try:
        file = open(filename, "r")
        for line in file:
            fields = line.strip().split(',')
            if fields[0].title() == lastName.title() and fields[1].title() == firstName.title():
                return line
    except FileNotFoundError:
        print("Contacts file not found.")
    except Exception as e:
        print(f"Error searching contacts: {e}")
    finally:
        file.close()

    return None

def modifyContact(originalFirstName, originalLastName, contacts_file, temp_file):
    existing_contact = searchContacts(originalFirstName, originalLastName, contacts_file)

    if existing_contact:
        print("Existing contact details:")
        printPerson(existing_contact)

        modified_fields = []

        for field in existing_contact.split(','):
            user_input = input(f"Enter new value for {field.strip()} (press Enter to keep the current value): ")
            modified_fields.append(user_input.strip() if user_input else field.strip())

        try:
            modified_contact = createContact(*modified_fields)
            print("Modified contact details:")
            printPerson(modified_contact)

            saveContact(modified_contact, contacts_file)
            removeContact(originalFirstName, originalLastName, contacts_file, temp_file)

            print("Contact has been modified.")
        except Exception as e:
            print(f"Error modifying contact: {e}")
    else:
        print("Contact not found.")

def removeContact(firstName, lastName, contacts_file, temp_file):
    try:
        originalFile = open(contacts_file, "r")
        tempFile = open(temp_file, "w")

        for line in originalFile:
            fields = line.strip().split(',')
            if fields[0].title() != lastName.title() or fields[1].title() != firstName.title():
                tempFile.write(line)
                
        originalFile.close()
        tempFile.close()
        
        os.remove(contacts_file)
        os.rename(temp_file, contacts_file)
        print("CONTACT WAS REMOVED")
    except FileNotFoundError:
        print("Contacts file not found.")
    except Exception as e:
        print(f"Error removing contact: {e}")
        

def Menu(contacts_file, temp_file):
    mainoptions = ("New entry", "Display contacts", "Search and display contact", "Modify contact", "Remove Contact","Exit")
    inputs = hmenu.getMenuCustomLetters(mainoptions)
    os.system("cls")
    try:
        if inputs == "NEW ENTRY":
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            pnumber = input("Enter Phone Number: ")

            other_args = ""
            other = input("Enter Other Information (or press Enter to finish): ")
            while other.strip():
                other_args += f",{other}"
                other = input("Enter Other Information (or press Enter to finish): ")
                os.system("cls")

            contactCSV = createContact(fname, lname, pnumber, other_args.lstrip(','))
            saveContact(contactCSV, contacts_file)
            Menu(contacts_file, temp_file)
            print("Contact CSV:", contactCSV)

        elif inputs == "DISPLAY CONTACTS":
            displayAll(contacts_file)
            Menu(contacts_file, temp_file)

        elif inputs == "SEARCH AND DISPLAY CONTACT":
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            result = searchContacts(fname, lname, contacts_file)
            if result:
                printPerson(result)
            else:
                print("Contact not found.")
            Menu(contacts_file, temp_file)

        elif inputs == "MODIFY CONTACT":
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            modifyContact(fname, lname, contacts_file, temp_file)
            Menu(contacts_file, temp_file)

        elif inputs == "REMOVE CONTACT":
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            removeContact(fname, lname, contacts_file, temp_file)
            Menu(contacts_file, temp_file)

        elif inputs == "EXIT":
            return

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    CONTACTS_FILE = "contacts.txt"
    TEMP_FILE = "temp_contacts.txt"
    Menu(CONTACTS_FILE, TEMP_FILE)
