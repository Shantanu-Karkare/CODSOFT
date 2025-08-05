contacts={}
def menu():
    print("1. Add contact:-")
    print("2. View contact:-")
    print("3. Search contact:-")
    print("4. Update contact:-")
    print("5. Delete contact:-")
    print("6 EXIT:-")

def add_contact():
    name=input("Enter Contact Name :-").lower()
    mobile_no=input("Enter Mobile Number:-")
    if not mobile_no.isdigit() or len(mobile_no)!=10:
        print("\"Please Enter a valid 10 digit mobile number\"\n")
        return
    email=input("Enter your Email:-")
    if "@gmail.com" not in email:
        print("Please enter a valid email\n")
        return
    address=input("Enter the Address:-")
    contacts[name.lower()]={
        "Mobile Number":mobile_no,
        "Email":email,
        "Address":address
    }
    print(f"Contact for {name} added successfully \n")  

def view_contact():
    if not contacts:
        print("No contacts found\n")
        return
    for name, i in contacts.items():
        print(f"Name:{name.title()}")
        for key, value in i.items():
          print(f"{key}:{value}")

def search_contact():
    name=input("Enter Name of contact:").lower()
    if name in contacts:
        print(f"Contact details of {name} are:")
        for key , value in contacts[name].items():
            print(f"{key}:{value}\n") 
    else:
        print("No contacts found:")

def update_contact():
   name=input("Enter contact name to update:").lower()
   if name in contacts:
    mobile_no=input("Enter updated Mobile Number:-")
    if not mobile_no.isdigit() or len(mobile_no)!=10:
        print("Please Enter a valid 10 digit mobile number\n")
        return
    email=input("Enter your updated Email:-")
    address=input("Enter updated address:-")  
    contacts[name.lower()]={
        "Mobile Number":mobile_no,
        "Email":email,
        "Address":address
    } 
    print(f"Contact details of {name.title()} is updated successfully")   
   else:
       print("No contact found\n")
def delete_contact():
    print("Enter the name of contact you want to delete?")
    name=input("Enter contact name:").lower()
    if name in contacts:
      confirm=input(f"are you sure you want to delete {name.title()} (yes/no) ?").lower() 
      if confirm=="yes":
         del contacts[name]
         print("Contact deleted Successfully \n!") 
    else:
        print("No contact found\n")
 
 #  Main body  
while True:
    print("=====Welcome=====")
    menu()
    choice = int(input("Enter the choice from (1-6): "))
    if choice == 1:
            add_contact()
    elif choice == 2:
            view_contact()
    elif choice == 3:
            search_contact()
    elif choice == 4:
            update_contact()
    elif choice == 5:
            delete_contact()
    elif choice == 6:
            print("Exiting Contact Book. Goodbye!")
            break
    else:
        print("Please enter a valid choice")
    




