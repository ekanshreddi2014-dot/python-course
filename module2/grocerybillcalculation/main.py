print("welcome to grocery bill calculater")
low_price = 0
medium_price = 0
high_price = 0
customers_served = 0
total_sales = 0
billing = True
while billing == True:
    name = input("whats you name ? : ")
    grocery_number = int(input("hoy many groceries do you have ? : "))
    if grocery_number <= 0:
        print("please print a valid number of items")
        continue
    customer_total = 0
    items_processed = 0
    while items_processed < grocery_number:
        item_name = input("whats the item ? : ")
        price = int(input("whats the price ? : "))
        quantity = int(input("how many do you have ? : "))
        if price <= 0 or quantity <= 0:
            print("invalid numbers please try again")
            continue
        cost_of_item = price * quantity
        customer_total += cost_of_item
        if price < 50:
            low_price += 1
        elif price < 200:
            medium_price += 1
        else:
            high_price += 1
        items_processed += 1
    customers_served += 1
    total_sales += customer_total
    another = input("Is there another customer? (yes/no): ")
    if another == "no":
        billing = False
print("--- FINAL REPORT ---")
print("Customers served:", customers_served)
print("Total sales:", total_sales,"rupees")
print("lower price : *")
print("medium price : /")
print("higher price : %")
for i in range(0,low_price):
    print("*")
for i in range(0,medium_price):
    print("/")
for i in range(0,high_price):
    print("%")
print("grocery billing complete")
            
            



    
    