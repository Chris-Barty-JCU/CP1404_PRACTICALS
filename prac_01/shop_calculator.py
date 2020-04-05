item_total = 0

n_items = int(input("Number of Items: "))

while n_items <= 0:
    print("Invalid Number Of Items!")
    n_items = int(input("Number of Items: "))

for x in range(1, n_items + 1, 1):
    item_cost = float(input("Price Of Item " + str(x) + ": "))
    item_total = item_total + item_cost
print("Total Price For " + str(n_items) + " Items Is: ${:.2f}".format(item_total))
