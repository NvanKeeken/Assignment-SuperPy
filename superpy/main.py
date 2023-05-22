# Imports
import argparse
from sys import stdout
import csv
from advance import advance_time, set_date_today, get_date_file, get_date_yesterday, get_month, get_date_now
from buy import buy_product
from sell import add_sold_product
from report import add_to_inventory, is_inStock, show_Inventory, make_inventory
from revenue import get_total_revenue
from profit import calculate_total_profit
# Do not change these lines
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"




# Your code below this line.
import argparse
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')
#All the subparsers 
sell = subparser.add_parser('sell')
buy = subparser.add_parser('buy')
report = subparser.add_parser("report")


# arguments subparser buy
buy.add_argument('--name', "-n", type=str, required=True, help="Give product name")
buy.add_argument('--price', "-p", type=float, required=True, help="Give product price")
buy.add_argument('--expiration_date',"-e", required=True, help="Give expiration date of the product")
buy.add_argument('--amount',"-a", required=True, help="Give amount of products bought")


# arguments subparser sell
sell.add_argument("--name", "-n", type=str, help="give product name of sold product", required=True )
sell.add_argument("--price", "-p", type=float, help="give price of product sold", required=True)
sell.add_argument("--amount", "-a", type=int, help="give amount of products sold")

# add argument report 
sub_report = report.add_subparsers(dest = "report_comment")
inventory = sub_report.add_parser("inventory")
revenue = sub_report.add_parser("revenue")
profit = sub_report.add_parser("profit")
inventory.add_argument("--now",nargs="?", const= get_date_now(), required=False, help="Shows inventory of actual date")
inventory.add_argument("--yesterday", nargs="?", const= get_date_yesterday(), required=False, help="Shows inventory of yesterday based on current date")
inventory.add_argument("--date",required=False, help="Give date you want the revnue form in format YYYY-mm-d")
inventory.add_argument("--today", nargs="?", const=get_date_file(), required=False, help="shows inventory what is precieved to be today")
# inventory.add_argument("--expired_products")

# adds arguments to subparser revenue from parser report 
revenue.add_argument("--today", nargs="?", const=get_date_file(), required=False, help="Gives revenue of today")
revenue.add_argument("--yesterday", nargs="?", const= get_date_yesterday(), required=False, help="Gives revenue of yesterday"  )
revenue.add_argument("--date", required=False, help="Give date you want the revnue form in format %Y-%m-%d")

# adds arguments to subparser 
profit.add_argument("--today", nargs="?", const=get_date_file(), required=False, help="Gives profit of today")
profit.add_argument("--yesterday", nargs="?", const= get_date_yesterday(), required=False, help="Gives profit of yesterday"  )
profit.add_argument("--date", required=False, help="Give date you want the profit form in format %Y-%m-%d")
# add argument advance
parser.add_argument("--advance_date", type=int,help="give an amount of days you want to advance by")



args = parser.parse_args()
if args.command == 'buy':
   print(args.name, args.price, args.expiration_date, args.amount)
   buy_product(args.name, args.price, args.expiration_date, args.amount)
  

if args.command == "sell":
   print(f"{args.name}{args.price}{args.amount}")
   is_inStock(args.name,args.price, args.amount)
#    sell_product(args.name, args.price)

elif args.command == 'report':
  print("report is made")
  if args.report_comment == "inventory":
     if args.yesterday:
        make_inventory(args.yesterday)
     if args.now:
        make_inventory(args.now)
     if args.date:
        make_inventory(args.date)
     if args.today:
        make_inventory(args.today)
     print(show_Inventory())

  if args.report_comment == "revenue":
     if args.today:
         print(args.today)
         stdout.write(f"Today's revenue: {get_total_revenue(args.today)} euro")
     elif args.yesterday:
         stdout.write(f"Yesterday's revenue: {get_total_revenue(args.yesterday)} euro")
     elif args.date:
        stdout.write(f"Revenue on {args.date}: {get_total_revenue(args.date)} euro")

  if args.report_comment == "profit":
     if args.today:
        stdout.write(f"Today's profit: {calculate_total_profit(args.today)} euro")
     elif args.yesterday:
         stdout.write(f"Yesterday's profit: {calculate_total_profit(args.yesterday)} euro")
     elif args.date:
         stdout.write(f"Profit in {get_month(args.date)}: {calculate_total_profit(args.date)} euro")

     
         
     
     
  
def main():
    pass


if args.advance_date:
    advance_time(args.advance_date)
else:
    set_date_today()
   
   


if __name__ == "__main__":
    main()
