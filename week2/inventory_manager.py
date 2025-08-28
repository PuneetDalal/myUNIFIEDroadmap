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
def main():
    """
    The main function to run the inventory management system application.
    """
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add New Item")
        print("2. View Inventory")
        # --- Placeholders for future features ---
        print("3. Update Item (Coming Soon)")
        print("4. Remove Item (Coming Soon)")
        print("5. Exit")
        print("-----------------------------------")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            # update_item() # We will build this next!
            print("Feature coming soon!")
        elif choice == '4':
            # remove_item() # And this one!
            print("Feature coming soon!")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()