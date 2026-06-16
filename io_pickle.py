import pickle

# The name of the file where we store the object

shoplistfile = 'shoplist.data'

# The list of things to buy

shoplist = ['apple', 'mange', 'carrot']
print(shoplist, "shoplist has been created")

# Write to the file

f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable

del shoplist
print("shoplist has been deleted")

# Read back from the storage 
f = open(shoplistfile, 'rb')
#load the object from the file 
storedlist = pickle.load(f)
print(storedlist)
f.close()
