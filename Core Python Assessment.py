import json
import os

class FruitManager:
    def __init__(self):
        self.fruit_stock = {}                       # Dictionary to store fruit stock
        self.log_file = "transaction_log.txt"
        self.stock_file = "fruit_stock.json"
        self.load_stock()

    def load_stock(self):                           # Load fruit stock from a file if it exists
        if os.path.exists(self.stock_file):
            with open(self.stock_file, "r") as file:
                self.fruit_stock = json.load(file)

    def save_stock(self):                           # Save fruit stock to a file.
        with open(self.stock_file, "w") as file:
            json.dump(self.fruit_stock, file, indent=4)

    def log_transaction(self, message):             # Log transactions to a log file.
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")

    def add_fruit(self, fruit_name, quantity):      # Add fruit stock.
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity
        self.save_stock()
        self.log_transaction(f"Added {quantity} of {fruit_name}.")

    def update_fruit(self, fruit_name, quantity):   # Update fruit stock.
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = quantity
            self.save_stock()
            self.log_transaction(f"Updated {fruit_name} to {quantity}.")
            return True
        return False

    def view_fruits(self):         # View current fruit stock.
        return self.fruit_stock

# customer.py
class Customer:
    def __init__(self, fruit_manager):
        self.fruit_manager = fruit_manager

    def view_stock(self):           # View available stock.
        stock = self.fruit_manager.view_fruits()
        if not stock:
            return "No fruits available in stock."
        return "\n".join([f"{fruit}: {quantity}" for fruit, quantity in stock.items()])

def display_menu():             # Display the main menu.
    menu = """
    Fruit Store Application
    1. Add Fruit Stock
    2. View Fruit Stock
    3. Update Fruit Stock
    4. Exit
    Enter your choice: """
    return menu

def main():
    fruit_manager = FruitManager()
    customer = Customer(fruit_manager)

    while True:
        try:
            print(display_menu())
            choice = input("Choose an option: ").strip()

            if choice == "1":
                fruit_name = input("Enter fruit name: ").strip().capitalize()
                quantity = int(input("Enter quantity: ").strip())
                fruit_manager.add_fruit(fruit_name, quantity)
                print(f"Successfully added {quantity} of {fruit_name}.")

            elif choice == "2":
                print("\nFruit Stock:")
                print(customer.view_stock())

            elif choice == "3":
                fruit_name = input("Enter fruit name: ").strip().capitalize()
                quantity = int(input("Enter updated quantity: ").strip())
                if fruit_manager.update_fruit(fruit_name, quantity):
                    print(f"Successfully updated {fruit_name} to {quantity}.")
                else:
                    print(f"Error: {fruit_name} not found in stock.")

            elif choice == "4":
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter appropriate values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()