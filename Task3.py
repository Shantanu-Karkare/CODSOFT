contacts={}
def menu():
    print("1. Add contact:-")
    print("2. View contact:-")
    print("3. Search contact:-")
    print("4. Update contact:-")
    print("5. Delete contact:-")
    print("1 EXIT:-")

def add_contact():
    name=input("Enter Contact Name :-").lower()
    mobile_no=input("Enter Mobile Number:-")
    if not mobile_no.isdigit():
        print("\"Please Enter a valid mobile number\"\n")
        return
    email=input("Enter your Email:-")
    if "@" not in email:
        print("Please enter a valid email\n")
        return
    adress=input("Enter the Adress:-")
    contacts[name.lower()]={
        "Moblie number":mobile_no,
        "Email":email,
        "Address":adress
    }
    print(f"Contact for {name} added successfully \n")  

def view_contact():
    if not contacts:
        print("No contacts found\n")
        return
    for name, i in contacts.items():
        print(f"Name:{name.title()}")
        for key, value in i.items():
          print(f"{key}:{value}\n")

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
    email=input("Enter your updated Email:-")
    adress=input("Enter updated adress:-")  
    contacts[name.lower()]={
        "Mobile Number":mobile_no,
        "Email":email,
        "Adress":adress
    } 

def delete_contact():
    print("Enter the name of contact you want to delete?")
    name=input("Enter contact name:").lower()
    if name in contacts:
      confirm=input(f"are you sure you want to delete {name.title()} (yes/no) ?").lower() 
      if confirm=="yes":
         del contacts[name]
         print("Contact deleted Successfully \n!")   
 
 #  Main body  
while True:
    print("=====Welcome=====")
    menu()
    choice=int(input("Enter the choice from(1-6):-"))
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        update_contact()
    elif choice==5:
        delete_contact()