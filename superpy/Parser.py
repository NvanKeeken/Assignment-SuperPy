import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")
buy = subparser.add_parser("buy", help="The action of buying an item")

buy.add_argument("--name", "-n", type=str, required=True, help="Give product name")
buy.add_argument("--price", "-p", type=float, required=True, help="Give product price")
buy.add_argument("--expiration", "-e", required=True, help="Give expiration date of the product")
buy.add_argument_group("amount", "-a", type=int, required=True, help="Give amount of product bought")
    



sell = subparser.add_parser("sell")

sell.add_argument("--name", "-n", type=str, help="give product name of sold product", required=True )
sell.add_argument("--price", "-p", type=float, help="give price of product sold", required=True)
sell.add_argument("--amount", "-a", type=int, help="give amount of products sold")

report = subparser.add_parser("report")
sub_report = report.add_subparsers(dest="report_command")
inventory = sub_report.add_parser("inventory")
revenue = sub_report.add_parser("revenue")
profit = sub_report.add_parser("profit")

advance = subparser.add_parser("advance")
args = parser.parse_args()
 
if args.command == "buy":
        print("hello im bougth")

print(create_parsers())