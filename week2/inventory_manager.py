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