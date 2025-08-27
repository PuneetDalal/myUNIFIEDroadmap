import pprint
inventory = {}
def add_items_single(inventory, n):
    item_id = input("Enter a unique Item ID: ") 
    inventory[item_id] = {}                        
    for i in range(n):                         
        Name = input(f"Enter name of item {i+1}: ")
        Price = input(f"Enter price for {Name}: ")
        inventory[item_id][Name] = Price           
    print("\nItem(s) added successfully under ID:", item_id)
    print("Current Inventory:")
    pprint.pprint(inventory)
def add_items_multiple(inventory, n, id_number):
    if id_number < 1:
        print("No item IDs created. Nothing added.")
    else:    
        for j in range(id_number):
            item_id = input(f"\nEnter unique Item ID {j+1}: ")
            inventory[item_id] = {}
            for i in range(n):
                Name = input(f"Enter name of item {i+1} for ID {item_id}: ")
                Price = input(f"Enter price for {Name}: ")
                inventory[item_id][Name] = Price 
    print("\nMultiple items added successfully.")
    print("Current Inventory:")
    pprint.pprint(inventory)

while True:
    choice = input("\nEnter 1 to add items or type 'exit' to quit: ").strip().lower()
    if choice == "exit":
        print("\nExiting Inventory Management System. Goodbye!")
        break
    elif choice == "1":
        respo = input("Do you want to store items under a single ID or different IDs? (s/d): ").lower()
        if respo not in ("s", "d"):
            print("Invalid input! Please enter 's' for single ID or 'd' for different IDs.")
        elif respo == "d":
            id_number = int(input("Enter how many unique IDs you want to create: "))
            n = int(input("Enter how many items per ID you want to add: "))
            add_items_multiple(inventory, n, id_number)
            print("\nInventory as list of items:")
            lst = list(inventory.items())
            print(lst)
        else:
            n = int(input("Enter number of items you want to add under a single ID: "))
            add_items_single(inventory, n)
            print("\nInventory as list of items:")
            lst = list(inventory.items())
            print(lst)
    else:
        print("Invalid option! Please enter '1' or 'exit'.")
