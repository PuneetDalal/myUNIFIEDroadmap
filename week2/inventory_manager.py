import pprint
inventory = {}
# inventory_manager.py
# Version 2.0 and later - Active Development
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