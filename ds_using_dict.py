#ab is sort for add 'a'ddress 'b'ook 

ab = {
    'Swaroop': 'swarroop@swaroopch.com', 
    'Larry': 'larry@well.org', 
    'Matsumoto': 'matz@ruby-lang.org', 
    'Spammer': 'Spammer@hotmail.com'
    }
print("Swaroop's address is", ab['Swaroop'])

#deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

#adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\n Guido's address is ", ab['Guido'] )


