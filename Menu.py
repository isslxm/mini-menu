import os

# List of electronic items with IDs and prices
items = {
    "smartphone": {"name": "Smartphone", "price": 500},
    "laptop": {"name": "Laptop", "price": 1000},
    "tablet": {"name": "Tablet", "price": 300},
    "smartwatch": {"name": "Smartwatch", "price": 200},
    "earbuds": {"name": "Wireless Earbuds", "price": 150},
    "console": {"name": "Gaming Console", "price": 400},
    "hard_drive": {"name": "External Hard Drive", "price": 80},
    "monitor": {"name": "Monitor", "price": 250},
    "keyboard": {"name": "Keyboard", "price": 50},
    "mouse": {"name": "Mouse", "price": 30},
    "speaker": {"name": "Portable Speaker", "price": 120},
    "tv": {"name": "Smart TV", "price": 800},
}

# Directory for storing receipts and reports
receipts_dir = "receipts"
if not os.path.exists(receipts_dir):
    os.makedirs(receipts_dir)

# Daily report file
daily_report_path = os.path.join(receipts_dir, "daily_report.txt")

def display_menu():
    print("\nWelcome to the Electronics Store!")
    print("Please select an item by its ID:")
    for item_id, info in items.items():
        print(f"{item_id} - {info['name']} - ${info['price']}")

def create_receipt(item_id, quantity, total_price):
    item_name = items[item_id]["name"]
    receipt_content = (
        f"Purchase Receipt\n"
        f"Item: {item_name}\n"
        f"Quantity: {quantity}\n"
        f"Price per unit: ${items[item_id]['price']}\n"
        f"Total Price: ${total_price}\n"
        f"Thank you for your purchase!\n"
    )
    
    # Create individual receipt file
    file_name = os.path.join(receipts_dir, f"{item_id}.txt")
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(receipt_content)
    
    print(f"\nReceipt saved to file: {file_name}")

    # Append to the daily report
    with open(daily_report_path, "a", encoding="utf-8") as report_file:
        report_file.write(
            f"Item: {item_name}, Quantity: {quantity}, Total Price: ${total_price}\n"
        )

def main():
    while True:
        display_menu()
        choice = input("\nEnter the item ID (or '0' to exit): ").strip()
        
        if choice == '0':
            print("Exiting the store. Thank you for visiting!")
            break

        if choice not in items:
            print("Invalid item ID. Please try again.")
            continue

        quantity = input("Enter quantity: ").strip()
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Please try again.")
            continue

        total_price = items[choice]["price"] * quantity
        print(f"\nYou selected: {items[choice]['name']}")
        print(f"Quantity: {quantity}")
        print(f"Total price: ${total_price}")
        
        create_receipt(choice, quantity, total_price)
        
        continue_shopping = input("\nWould you like to buy another item? (yes/no): ").strip().lower()
        if continue_shopping != 'yes':
            print("Thank you for shopping with us! Goodbye.")
            break

if __name__ == "__main__":
    main()
