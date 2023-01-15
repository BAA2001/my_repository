# Do not modify these lines
__winc_id__ = "62311a1767294e058dc13c953e8690a4"
__human_name__ = "casting"

# Add your code after this line
leek_price = 2

print(f'Leek is" + " " + str(leek_price) + " " + "euro per kilo."')

four_leeks = "leek 4"
four_leeks_number_ext = int(four_leeks[four_leeks.find(" ") :])
sum_total = leek_price * four_leeks_number_ext

broccoli_price = 2.34
order = "broccoli 1.6"
order_number_ext = float(order[order.find(" ") :])
broccoli_total_price = broccoli_price * order_number_ext
broccoli_total_price_rounded = round(broccoli_total_price, 2)
print(f"{order_number_ext} kg broccoli costs {broccoli_total_price_rounded} ")
