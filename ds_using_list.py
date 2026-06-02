#This is my Shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("I have ", len(shoplist), "items to purchase")
print("These items are : ", end=' ')
for items in shoplist:
    print(items, end=" ")
print("\nI also have to buy rice.")
shoplist.append('rice')
print("My shopping list is now ", shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted Shopping list is ', shoplist)
print('The first item I will buy is ', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the ', olditem)
print("My Shopping list now ", shoplist)