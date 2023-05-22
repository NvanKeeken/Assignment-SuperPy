import csv
from advance import get_date_file

def get_file_id(csv_path):
   with open(csv_path, 'r') as file:
       csvreader = csv.reader(file)
       next(csvreader)
       count = 0
       for row in csvreader:
           count += 1
       return count +1

def get_bought_id(product_name):
   with open("bought.csv", "r") as boughtfile:
      reader = csv.DictReader(boughtfile)
      bought_id = ""
      for row in reader:
       if row["product_name"] == product_name:
          bought_id += row["id"]
          return bought_id
   
  
        
   
def add_sold_product(product_name, sell_price, amount):

    with open("sold.csv", 'a', newline="") as soldfile:
     writer = csv.writer(soldfile, lineterminator='\n')
     
    #  writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])
     sell_date = get_date_file()
     sold_id = get_file_id("sold.csv")
     bought_id = get_bought_id(product_name)
     product =[sold_id,bought_id,amount,sell_date, sell_price]
     writer.writerow(product)
     soldfile.close()


       
     
         

print(get_file_id("sold.csv"))
