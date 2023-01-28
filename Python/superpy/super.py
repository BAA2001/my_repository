# Imports
import os
import argparse
import pandas as pd
from datetime import datetime, timedelta
from dateutil.parser import parse
from termcolor import colored
from tabulate import tabulate

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# Principles
parser = argparse.ArgumentParser(
    prog="SuperPy",
    description="Record and track purchases and sales of items.",
)
parser.add_argument(
    "--set_time",
    type=str,
    default=datetime.now().strftime("%Y-%m-%d"),
    help="Set the date for which the report is generated in format %Y-%m-%d",
)

commands = parser.add_subparsers(dest="command")

buy = commands.add_parser("buy", help="Record a purchase of an item.")
buy.add_argument(
    "-bn", "--bname", type=str, required=True, help="Name of the item being bought."
)
buy.add_argument(
    "-bc",
    "--bcount",
    type=int,
    default=1,
    help="Number of items purchased (default: 1)",
)
buy.add_argument(
    "-bp", "--bprice", type=float, required=True, help="Price of the item."
)
buy.add_argument("-bd", "--bdate", type=str)
buy.add_argument(
    "-e",
    "--expiration",
    type=str,
    required=True,
    help="Expiration date of the item in format of %Y-%m-%d",
)

sell = commands.add_parser("sell", help="Record a sale of an item.")
sell.add_argument(
    "-sn", "--sname", type=str, required=True, help="Name of the item being sold."
)
sell.add_argument(
    "-sc", "--scount", type=int, default=1, help="Number of items sold (default: 1)"
)
sell.add_argument(
    "-sp", "--sprice", type=float, required=True, help="Price of the item."
)
sell.add_argument(
    "-sd",
    "--sdate",
    type=str,
    default=datetime.now().strftime("%Y-%m-%d"),
    help="Sell date of the item in format of %Y-%m-%d",
)

report = commands.add_parser(
    "report", help="Generate reports on inventory, revenue and profit."
)
report.add_argument(
    "-i",
    "--inventory",
    type=str,
    help="generate report on inventory",
)
report.add_argument("-r", "--revenue", type=str, help="generate report on revenue")
report.add_argument("-p", "--profit", type=str, help="generate report on profit")

args = parser.parse_args()

# Global variable to store the current date
today = datetime.now().strftime("%Y-%m-%d")

# Function to set the date


def set_time(date=None):
    global today
    if date:
        try:
            # Format the date to YYYY-MM-DD
            today = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format, please use %Y-%m-%d")
    else:
        today = datetime.now().strftime("%Y-%m-%d")


# Set the date if the --set_time argument is provided
if args.set_time:
    set_time(args.set_time)
    now = datetime.strptime(today, "%Y-%m-%d")
    if args.set_time == "today":
        date_obj = now
        print(colored(f"Current date: {date_obj}", "magenta"))
    elif args.set_time == "yesterday":
        date_obj = now - timedelta(days=1)
        print(colored(f"Current date: {date_obj}", "magenta"))
    else:
        print(colored(f"Current date: {args.set_time}", "magenta"))

args.bname = args.bname.lower()
args.sname = args.sname.lower()


def to_buy():

    # record buying in separate .csv file
    def record_buying():
        b_file = str(os.path.abspath("bought.csv"))
        args.bdate = datetime.now().date()

        if not os.path.exists("bought.csv") or os.path.getsize(b_file) == 0:
            b_df = pd.DataFrame(columns=["Name", "Buy Count", "Buy Price", "Date"])
            b_df.to_csv(b_file, index=False)

        b_df = pd.read_csv(b_file)
        b_df["Date"] = pd.to_datetime(datetime.now())

        # Check if the name is already present in the dataframe
        if args.bname in b_df["Name"].values:
            # Update the count for the corresponding name
            b_df.loc[b_df["Name"] == args.bname, "Buy Count"] += args.bcount  # type: ignore
        else:
            # Append a new row to the dataframe
            data = {
                "Name": args.bname,
                "Buy Count": args.bcount,
                "Buy Price": args.bprice,
                "Date": args.bdate,
            }
            b_df_nrow = pd.DataFrame(data, columns=b_df.columns, index=[len(b_df)])
            b_df = pd.concat([b_df, b_df_nrow], ignore_index=True)

        # Write the updated dataframe to the file
        b_df.to_csv(b_file, index=False)

    record_buying()

    # Get the file path
    file = str(os.path.abspath("inventory.csv"))

    # Create a new file for inventory and buy record if they don't exist or are empty
    if not os.path.exists("inventory.csv") or os.path.getsize(file) == 0:
        df = pd.DataFrame(
            columns=["Name", "Count", "Price", "Expiration", "Date of Addition"]
        )
        df.to_csv(file, index=False)

    # parse expiration date
    date_object = parse(args.expiration)

    # Read the existing data from the file
    df = pd.read_csv(file)

    # Check if the name is already present in the dataframe
    if args.bname in df["Name"].values:
        # Update the count for the corresponding name
        df.loc[df["Name"] == args.bname, "Count"] += args.bcount  # type: ignore
        c = int(df.loc[df["Name"] == args.bname, "Count"])  # type: ignore
        print(colored(f"You now have {c} of {args.bname}", "green"))
    else:
        # Append a new row to the dataframe
        data = {
            "Name": args.bname,
            "Count": args.bcount,
            "Price": args.bprice,
            "Expiration": date_object,
            "Date of Addition": datetime.now().date().strftime("%Y-%m-%d"),
        }
        df_new_row = pd.DataFrame(data, columns=df.columns, index=[len(df)])
        df = pd.concat([df, df_new_row], ignore_index=True)
        print(
            colored(
                f"You bought {args.bcount} of {args.bname} for the price of {args.bprice}. Expiration date: {date_object}",
                "green",
            )
        )

    # Write the updated dataframe to the file
    df.to_csv(file, index=False)


def to_sell():
    try:

        def record_selling():

            inventory_file = str(os.path.abspath("inventory.csv"))

            inventory_df = pd.read_csv(inventory_file)

            # Check if the item is expired
            item_expiry = inventory_df[inventory_df["Name"] == args.sname]["Expiration"]
            if (
                len(item_expiry) > 0 and pd.to_datetime(item_expiry.iat[0]).date() < datetime.now().date()  # type: ignore
            ):
                inventory_df = inventory_df[inventory_df.Name != args.sname]
                return

            sold_file = str(os.path.abspath("sold.csv"))

            if not os.path.exists("sold.csv") or os.path.getsize(sold_file) == 0:
                s_df = pd.DataFrame(
                    columns=["Name", "Sell Count", "Sell Price", "Date"]
                )
                s_df.to_csv(sold_file, index=False)

            s_df = pd.read_csv(sold_file)
            s_df["Date"] = pd.to_datetime(s_df["Date"], format="%Y-%m-%d")

            # Check if the name is already present in the dataframe
            if args.sname in s_df["Name"].values:
                # Update the count for the corresponding name
                s_df.loc[s_df["Name"] == args.sname, "Sell Count"] += args.scount  # type: ignore
            elif args.scount > inventory_df.loc[inventory_df["Name"] == args.sname, "Count"].iat[0]:  # type: ignore
                return
            else:
                # Append a new row to the dataframe
                data = {
                    "Name": args.sname,
                    "Sell Count": args.scount,
                    "Sell Price": args.sprice,
                    "Date": args.sdate,
                }
                s_df_nrow = pd.DataFrame(data, columns=s_df.columns, index=[len(s_df)])
                s_df = pd.concat([s_df, s_df_nrow], ignore_index=True)

            # Write the updated dataframe to the file
            s_df.to_csv(sold_file, index=False)

        record_selling()

        # Get the file paths
        file = str(os.path.abspath("inventory.csv"))

        # Check if file is empty
        if os.path.getsize(file) == 0:
            print(colored("The store is empty! Try to buy an item first.", "red"))
            return

        # Read the existing data from the file
        df = pd.read_csv(file)

        # parse the expiration date column
        df["Expiration"] = pd.to_datetime(df["Expiration"])

        # Check if the requested item has expired
        item_expiry = df[df["Name"] == args.sname]["Expiration"]
        if len(item_expiry) > 0 and item_expiry.iat[0] < datetime.now():
            print(colored(f"{args.sname} has expired!", "red"))
            df = df[df.Name != args.sname]
        # Check if item is in inventory
        elif not df["Name"].isin([args.sname]).any():  # type: ignore
            print(
                colored(
                    "I'm sorry, we don't have this quantity of the items in stock.",
                    "red",
                )
            )
            return
        # Check if sell amount is greater than inventory amount
        else:
            if args.scount > df.loc[df["Name"] == args.sname, "Count"].iat[0]:  # type: ignore
                print(
                    colored(
                        "I'm sorry, we don't have this quantity of this item in stock.",
                        "red",
                    )
                )
                return
            # Reduce amount in inventory after selling
            df.loc[df["Name"] == args.sname, "Count"] -= args.scount
            print(colored(f"You have sold {args.scount} of {args.sname} ", "green"))
            # Remove item if the amount drops to 0
            if df.loc[df["Name"] == args.sname, "Count"].iat[0] <= 0:  # type: ignore
                df = df[df.Name != args.sname]
                print(colored(f"{args.sname.title()} is out of stock", "red"))

        # Write the updated dataframe to the file
        df.to_csv(file, index=False)
    except FileNotFoundError:
        print(
            colored("No inventory yet... Please make a purchase to create one.", "red")
        )


def to_report():

    # Get the absolute path of the inventory file
    inventory_file = str(os.path.abspath("inventory.csv"))
    bought_file = str(os.path.abspath("bought.csv"))
    sold_file = str(os.path.abspath("sold.csv"))

    # Check if inventory argument is given
    if args.inventory:
        try:
            # Check if the inventory file is empty
            if os.path.getsize(inventory_file) == 0:
                print(colored("The store is empty! Try to buy an item first.", "red"))
            elif not os.path.exists(inventory_file):
                print(colored("No inventory yet", "red"))
            else:
                # Read the inventory data from the file
                inventory_df = pd.read_csv(inventory_file)
                inventory_df["Date of Addition"] = inventory_df[
                    "Date of Addition"
                ].astype(str)
                inventory_df["Expiration"] = inventory_df["Expiration"].astype(str)
                # Convert the date columns to datetime type
                inventory_df["Date of Addition"] = pd.to_datetime(
                    inventory_df["Date of Addition"], format="%Y-%m-%d"
                )
                inventory_df["Expiration"] = pd.to_datetime(
                    inventory_df["Expiration"], format="%Y-%m-%d"
                )

                # Check if the inventory dataframe is empty
                if inventory_df.shape[0] == 0:
                    print(
                        colored(
                            "The store is empty! Try to buy an item first.",
                            "red",
                        )
                    )
                    return

                # Set time
                now = datetime.strptime(today, "%Y-%m-%d")

                # Get the date object based on the inventory argument
                try:
                    if args.inventory == "now":
                        date_obj = now
                    elif args.inventory == "today":
                        date_obj = now
                    elif args.inventory == "yesterday":
                        date_obj = now - timedelta(days=1)
                    else:
                        date_obj = parse(args.inventory)
                except ValueError:
                    print(
                        colored(
                            "Wrong format. Please use the format %Y-%m-%d",
                            "red",
                        )
                    )
                    return

                # Filter the inventory dataframe based on the date object
                inventory_df_filtered = inventory_df[
                    inventory_df["Date of Addition"].dt.date == date_obj.date()
                ]

                # Print the filtered inventory
                print(
                    tabulate(inventory_df_filtered, headers="keys", tablefmt="pretty")
                )

        except FileNotFoundError:
            print(
                colored(
                    "No inventory yet... Please make a purchase to create one.", "red"
                )
            )

    # Check if revenue argument is given
    if args.revenue:
        try:
            # Check if the inventory file is empty
            if os.path.getsize(sold_file) == 0:
                print(
                    colored("The store is empty! Try to buy some an item first.", "red")
                )
            else:
                # Read the sold data from the file
                s_df = pd.read_csv(sold_file, parse_dates=["Date"])

                # Check if the inventory dataframe is empty
                if s_df.shape[0] == 0:
                    print(
                        colored(
                            "The store is empty! Try to buy an item first.",
                            "red",
                        )
                    )
                    return

                # Set time
                now = datetime.strptime(today, "%Y-%m-%d")

                # Get the date object based on the inventory argument
                try:
                    if args.inventory == "now":
                        date_obj = now
                    elif args.revenue == "today":
                        date_obj = now
                    elif args.revenue == "yesterday":
                        date_obj = now - timedelta(days=1)
                    else:
                        date_obj = parse(args.revenue)
                except ValueError:
                    print(
                        colored("Wrong format. Please use the format %Y-%m-%d"), "red"
                    )
                    return

                # Filter the dataframe based on the date object
                s_df_filtered = s_df[s_df["Date"].dt.date == date_obj.date()]
                # Calculate the sum of the selling revenue
                revenue = (
                    s_df_filtered["Sell Count"] * s_df_filtered["Sell Price"]
                ).sum()

                # Print the revenue
                print(colored(f"Revenue: {revenue}", "yellow"))
        except FileNotFoundError:
            print(
                colored(
                    "No revenue to record yet... Please make a sell to create one.",
                    "red",
                )
            )

    # Check if profit argument is given
    if args.profit:
        try:
            # Check if both the bought and sold files are empty
            if os.path.getsize(bought_file) == 0 or os.path.getsize(sold_file) == 0:
                print(
                    colored("The store is empty! Try to buy some an item first.", "red")
                )
                return
            # Read the bought data from the file
            bought_df = pd.read_csv(bought_file, parse_dates=["Date"])
            # Read the sold data from the file
            sold_df = pd.read_csv(sold_file, parse_dates=["Date"])

            # Check if the inventory dataframe is empty
            if bought_df.shape[0] == 0 or sold_df.shape[0] == 0:
                print(colored("The store is empty! Try to buy an item first.", "red"))
                return

            # Set time
            now = datetime.strptime(today, "%Y-%m-%d")

            # Get the date object based on the inventory argument
            try:
                if args.profit == "now":
                    date_obj = now
                elif args.profit == "today":
                    date_obj = now
                elif args.profit == "yesterday":
                    date_obj = now - timedelta(days=1)
                else:
                    date_obj = parse(args.profit)
            except ValueError:
                print(colored("Wrong format. Please use the format %Y-%m-%d", "red"))
                return

            # Filter the dataframe based on the date object
            bought_df_filtered = bought_df[bought_df["Date"].dt.date == date_obj.date()]
            sold_df_filtered = sold_df[sold_df["Date"].dt.date == date_obj.date()]

            # Calculate the expense from the filtered dataframe
            expense = -abs(
                bought_df_filtered["Buy Count"] * bought_df_filtered["Buy Price"]
            ).sum()
            # Calculate the revenue from the filtered dataframe
            revenue = (
                sold_df_filtered["Sell Count"] * sold_df_filtered["Sell Price"]
            ).sum()
            # Calculate the profit
            profit = expense - revenue
            # Print the profit
            if profit <= 0:
                print(colored(f"Profit:0 ({round(profit, 2)})", "red"))
            else:
                print(colored(f"Profit: {round(profit, 2)}", "yellow"))
        except FileNotFoundError:
            print(
                colored(
                    "No profit to record yet... Please make a purchase and/or sell to create one.",
                    "red",
                )
            )


if args.command == "buy":
    to_buy()
if args.command == "sell":
    to_sell()
if args.command == "report":
    to_report()
