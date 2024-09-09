#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## project name
    #Shop inventory Management System:
products = {
    101: {"name": "sugar", "quantity": 10},
    102: {"name": "Salt", "quantity": 20},
    103: {"name": "Oil", "quantity": 30}
}

def check_availability():
    product_id = int(input("Enter product ID: "))
    if product_id in products:
        product = products[product_id]
        if product["quantity"] > 0:
            print(f"{product['name']} is available. Quantity: {product['quantity']}")
        else:
            print(f"{product['name']} is out of stock.")
    else:
        print("Product not found.")

def update_inventory():
    product_id = int(input("Enter product ID: "))
    if product_id in products:
        new_quantity = int(input("Enter new quantity: "))
        products[product_id]["quantity"] = new_quantity
        print("Inventory updated.")
    else:
        print("Product not found.")

def add_product():
    product_id = int(input("Enter new product ID: "))
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    products[product_id] = {"name": product_name, "quantity": quantity}
    print("Product added.")

def remove_product():
    product_id = int(input("Enter product ID to remove: "))
    if product_id in products:
        del products[product_id]
        print("Product removed.")
    else:
        print("Product not found.")

while True:
    print("\nOptions:")
    print("1. Check A1vailability")
    print("2. Update Inventory")
    print("3. Add Product")
    print("4. Remove Product")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        add_product()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please choose again.")



# In[ ]:





# In[ ]:





# In[ ]:




