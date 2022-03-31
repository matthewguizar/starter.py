cup_invoices = open("CupcakeInvoices.csv")

# for all_rows in cup_invoices:
#     print (all_rows)

# for flavor in cup_invoices:
#     flavor = flavor.rstrip('\n').split(',')
#     print(flavor[2])


for price in cup_invoices:
    price = price.split(',')
    total = int(price[3]) * float(price[4])

    # print(total)
    
total = 0

for 