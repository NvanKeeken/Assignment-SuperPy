import csv
import pandas as pd
from sell import add_sold_product
from advance import get_date_file
import datetime
from revenue import get_sold_products_per_date
from profit import get_bought_products_by_date

def reset_inventory():
    with open("Invent.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Count", "Buy Price", "Expiration Date"])

def show_Inventory():
       df = pd.read_csv("Invent.csv")
       print(df)
print(show_Inventory())


def is_inStock(product_name,price, amount):
    with open("Invent.csv", "r") as file:
        writer = csv.DictReader(file)
        is_in_stock = False
        for row in writer:
            if row["Product Name"] == product_name:
                if int(row["Count"]) == int(amount):
                    is_in_stock = True
                    delete_product(row)
                if int(row["Count"]) > 0 and int(row["Count"]) >= int(amount):
                    is_in_stock = True
                    update_count_inventory(product_name,"sold", amount)
        if is_in_stock:
            add_sold_product(product_name, price, amount)
        elif expiration_check(row):
             delete_product(row)
             print("Product(s) are expired")
        else:
            print("Error: product is out of stock")
            

def delete_product(product_row): 
    newLines = []
    with open("Invent.csv", "r+") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if line != product_row:
                newLines.append(line)
        reset_inventory()
        for line in newLines:
             with open("Invent.csv", "a", newline="") as file:
                 writer = csv.writer(file)
                 writer.writerow([line["Product Name"], line["Count"], line["Buy Price"], line["Expiration Date"]])
     

def update_count_inventory(product_name,status, amount = 1): 
    newLines = []
    with open("Invent.csv", "r+") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            count = int(line["Count"]) - int(amount) if status == "sold" else int(line["Count"]) + int(amount)
            if line["Product Name"] == product_name:
                newLines.append(
                    {
                        "Product Name": line["Product Name"],
                        "Count": count,
                        "Buy Price": line["Buy Price"],
                        "Expiration Date": line["Expiration Date"]
                    }
                )
            else:
                newLines.append(line)
        reset_inventory()
        for line in newLines:
             with open("Invent.csv", "a", newline="") as file:
                 writer = csv.writer(file)
                 writer.writerow([line["Product Name"], line["Count"], line["Buy Price"], line["Expiration Date"]])


def add_to_inventory(product_name, buy_price, expiration_date, status, amount):
       with open("Invent.csv", "r") as file:
           csvreader = csv.DictReader(file)
           is_inStock = False
           for row in csvreader:
               print(row["Product Name"] == product_name)
               if row["Product Name"] == product_name:
                   is_inStock = True
           if is_inStock:
             update_count_inventory(product_name, status, amount)
           else:
            #  with open("Invent.csv") as f:
            #     csvreader = csv.DictReader(f)
                with open("Invent.csv", "a", newline="") as inventoryfile:
                   csvwriter = csv.writer(inventoryfile)
                   csvwriter.writerow([product_name,amount, buy_price, expiration_date])

#  Dit is allemaal een expiriment om expiration date te checkken en te zorgen dat inventory van verleden kunt opvragen
def expiration_check(row):
     current_date = datetime.datetime.strptime(get_date_file(), "%Y-%m-%d")
     row_date = datetime.datetime.strptime(row["Expiration Date"], "%Y-%m-%d")
     is_expired= False
     if row_date.date() > current_date.date():
        is_expired += False
     else:
        is_expired += True
# Dit werkt het filterd de producten voor een bepaalde datum
def get_products_before(date, csv_path, product_date ):
     products = []
     with open(csv_path, "r") as file:
       reader = csv.DictReader(file)
       for row in reader:
         inventorydate = datetime.datetime.strptime(date, "%Y-%m-%d")
         row_date = datetime.datetime.strptime(row[product_date], "%Y-%m-%d")
         if row_date <= inventorydate:
            products.append(row)
       return products
     
""" calculates al products bought before or on a certain date, and does the same for sold products
if a bought product in that list is also in the sold products list, calculate amount of bought products minus sold products 
if that difference is not zero append it to the new inventory, if bought product is not part of sold product list append it 
as well to the new inventory """
def make_inventory(date):
    sold_products = get_products_before(date, "sold.csv", "sell_date")
    bought_products = get_products_before(date, "bought.csv", "buy_date")
    print("sold", sold_products)
    print("bought",bought_products)
    new_inventory =[]
    
    for bought_product in bought_products:
             sold_id = find_sold_product(bought_product["id"],sold_products, "bought_id")
             sold_amount = find_sold_product(bought_product["id"],sold_products, "amount")
             if  bought_product["id"] == sold_id:
                print("amount",find_bought_product(bought_product["id"],"sold.csv", "bought_id"))
                amount_difference = int(bought_product["amount"]) - int(sold_amount)
                print("difference",amount_difference)
                if amount_difference != 0:
                    # bought_product.update({"amount":amount_difference })
                    new_inventory.append(
                    {
                        "Product Name": bought_product["product_name"],
                        "Count": amount_difference,
                        "Buy Price": bought_product["buy_price"],
                        "Expiration Date": bought_product["expiration_date"]
                    })      
             else:
                      new_inventory.append({
                        "Product Name": bought_product["product_name"],
                        "Count": bought_product["amount"],
                        "Buy Price": bought_product["buy_price"],
                        "Expiration Date": bought_product["expiration_date"]
                    }) 
    reset_inventory()  
    pass_to_inventory(new_inventory)
    return new_inventory

def pass_to_inventory(new_inventory):
    print("hello", new_inventory)
    for line in new_inventory:
       with open("Invent.csv", "a", newline="") as file:
           writer = csv.writer(file)
           writer.writerow([
                line["Product Name"],
                line["Count"],
                line["Buy Price"],
                line["Expiration Date"] ])


def find_bought_product(id,path,characteristic):
    with open(path, "r") as boughtproduct:
        reader= csv.DictReader(boughtproduct)
        for row in reader:
            # print(row, id)
            if id == row["bought_id"]:
                   return row[characteristic]
            
def find_sold_product(id,products_list,characteristic):
        for product in products_list:
            if id == product["bought_id"]:
                   return product[characteristic]
            
             
# def get_inventory_by_date(date):
#     sold_products_today = get_sold_products_per_date(date)
#     bought_product_today = get_bought_products_by_date(date)
#     for product in sold_products_today:
#         buy_price = find_bought_product(product["bought_id"], "buy_price")
#         expiration_date = find_bought_product(product["bought_id"], "expiration_date")
#         add_to_inventory(product["product_name"], buy_price,expiration_date, "bought", product["amount"] )
#     for product in bought_product_today:
#         with open("Invent.csv", "r") as file:
#             reader = csv.DictReader(file)
#             is_in_stock = False
#             for row in writer:
#                 if row["Product Name"] == product["product_name"]:
#                     if int(row["Count"]) == int(product["amount"]):
#                         delete_product(row)
#                     if int(row["Count"]) > 0 and int(row["Count"]) >= int(product["amount"]):
#                         is_in_stock = True
#                         update_count_inventory(product["product_name"],"sold", product["amount"])
#         #  (product["product_name"],product["buy_price"],product["expiration_date"], "sold", product["amount"] )
        
print(make_inventory("2023-05-20"))






   

            