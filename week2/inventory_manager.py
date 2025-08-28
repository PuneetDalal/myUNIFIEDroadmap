import pprint
inventory = {}
# inventory_manager.py
def add_item():
    """
    Adds a single, well-structured item to the inventory.
    Handles data validation for price and quantity.
    """
    item_id = input("Enter the unique ID for the new item: ").strip()
    if item_id in inventory:
        print(f"\nError: Item ID '{item_id}' already exists. Please choose a unique ID.")
        return

    item_name = input("Enter the item name: ").strip()
    
    #--- Data Validation 2: Ensure numbers are actually numbers ---
    try:
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
    except ValueError:
        print("\nError: Invalid input. Price and Quantity must be numbers. Item not added.")
        return

    #--- This is the core structural change ---
    inventory[item_id] = {
        "name": item_name,
        "price": item_price,
        "quantity": item_quantity
    }
    
    print(f"\nSuccess! Item '{item_name}' (ID: {item_id}) was added.")
def view_inventory():
    """ADDED the feature of view inventory .
    deletion and updateing element features coming soon"""
    print("---    Inventory    ---")
    if not inventory:
        print("The inventory is currently empty.")
        return
    print(f"{'ID':<10}|{'Name':<20}|{'Price':<10}|{'Quantity':<10}")
    print("_"*90)
    for item_id,details in inventory.items():
        name=details['name']
        price = details['price']
        quantity = details['quantity']
        print(f"{item_id:<10} | {name:<20} | ${price:<9.2f} | {quantity:<10}")
        print("_"*90)
def remove_item():
    x = input("Enter the unique ID of the item you want to delete: ").strip()
    
    if x in inventory:
        removed_item = inventory.pop(x)  # removes and returns the item details
        print(f"\nSuccess! Item with ID '{x}' ({removed_item['name']}) has been removed successfully.")
    else:
        print("\nError: The ID doesn't exist in the inventory!")
def update_item():
    item_id = input("Enter the unique ID of the item you want to update: ").strip()
    
    if item_id not in inventory:
        print(f"\nError: Item ID '{item_id}' not found in inventory.")
        return
    
    item = inventory[item_id]
    print(f"\nCurrent details of '{item_id}': {item}")
    
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Price")
    print("3. Quantity")
    print("4. All fields")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        new_name = input("Enter new name: ").strip()
        item["name"] = new_name
    elif choice == "2":
        try:
            new_price = float(input("Enter new price: "))
            item["price"] = new_price
        except ValueError:
            print("Error: Price must be a number.")
            return
    elif choice == "3":
        try:
            new_quantity = int(input("Enter new quantity: "))
            item["quantity"] = new_quantity
        except ValueError:
            print("Error: Quantity must be an integer.")
            return
    elif choice == "4":
        new_name = input("Enter new name: ").strip()
        try:
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
        except ValueError:
            print("Error: Price must be a number and Quantity must be an integer.")
            return
        item["name"] = new_name
        item["price"] = new_price
        item["quantity"] = new_quantity
    else:
        print("Invalid choice. Update cancelled.")
        return
    
    print(f"\nSuccess! Item '{item_id}' has been updated to: {item}")
def main():
    """
    The main function to run the inventory management system application.
    """
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add New Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")
        print("-----------------------------------")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_item()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()