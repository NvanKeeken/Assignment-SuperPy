import csv
from sell import get_file_id
from advance import get_date_file
from report import add_to_inventory

# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter="|")
#     writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])

def buy_product(product_name, buy_price, expiration_date, amount):
    add_to_inventory(product_name,buy_price, expiration_date, "bought", amount )
    with open("bought.csv", 'a', newline="") as file:
     writer = csv.writer(file, lineterminator='\n')
     
    #  writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])
     bought_id = get_file_id("bought.csv")
     buy_date = get_date_file()
     product =[bought_id,product_name,buy_date,buy_price,expiration_date,amount]
     writer.writerow(product)
     file.close()
     
