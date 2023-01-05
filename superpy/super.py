# Imports
import os
import argparse
import csv
import pandas as pd
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# principles
parser = argparse.ArgumentParser(prog="SuperPy")
subparser = parser.add_subparsers()

buy = subparser.add_parser("buy")
sell = subparser.add_parser("sell")
report = subparser.add_parser("report")

buy.add_argument("--id", type=int)
buy.add_argument("-n", "--name", type=str)
buy.add_argument("-c", "--count", type=int, default=1)
buy.add_argument("-p", "--price", type=float)
buy.add_argument("-e", "--expiration", type=str)

sell.add_argument("--b_id", type=int)
sell.add_argument("-id", "--bought_id", type=int)
sell.add_argument("-d", "--sell_date", type=str)
sell.add_argument("-p", "--sell_price", type=float)

args = parser.parse_args()

# print buy status
class buy:

    print(
        f"OK, you have bought {args.count} {args.name}('s) for the price of {args.price}$. Its expiry date is {args.expiration}"
    )

    # record buying
    filename = "bought.csv"
    header = [
        "ID",
        "Product Name",
        "Count",
        "Buy Price",
        "Expiration Date",
    ]
    # HEADER MANAGEMENT
    def buy_header(filename=filename, header=header):
        if os.path.exists(filename) == False:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
        else:
            with open(filename, "r") as file:
                reader = [row for row in csv.DictReader(file)]
                if len(reader) == 0:
                    with open(filename, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(header)

    buy_header()

    # WRITE DATA
    def buy_data(filename=filename, header=header):
        with open(filename, "r") as rf, open(filename, "a", newline="") as af:
            reader = [row for row in csv.DictReader(rf)]
            writer = csv.DictWriter(af, fieldnames=header)

            id = len(reader) + 1

            # DATA
            data = {
                "ID": id,
                "Product Name": args.name.lower(),
                "Count": args.count,
                "Buy Price": args.price,
                "Expiration Date": args.expiration,
            }

            writer.writerow(data)

    buy_data()

    filename = "bought.csv"
    with open(filename) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            print(row)


if __name__ == "__main__":
    buy


# which products does the supermarket offer?
# How many of each type of product does the supermarket hold currently?
# How much was each product bought for?
# What is the expiry date of the bought product(s)
# How much was each product sold for or are they expired?
