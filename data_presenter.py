cup_invoices = open("CupcakeInvoices.csv")

# for all_rows in cup_invoices:
#     print (all_rows)

# for flavor in cup_invoices:
#     flavor = flavor.rstrip('\n').split(',')
#     print(flavor[2])


# for i_price in cup_invoices:
#     i_price = i_price.split(',')
#     i_total = int(i_price[3]) * float(i_price[4])

    # print(i_total)
    
total = 0

# for t_price in cup_invoices:
#     t_price = t_price.split(',')
#     total = total + int(t_price[3]) * float(t_price[4])
# print(total)

cup_invoices.close()