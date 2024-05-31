from collections import namedtuple

clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]


ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)

coat_cost = new_coat.price

updated_clothes_data = []
for elem in clothes:
  updated_clothes_data.append(ClothingItem(elem[0], elem[1], elem[2], elem[3]))

print(updated_clothes_data)
Got me this:

[ClothingItem(type='t-shirt', color='green', size='large', price=9.99), ClothingItem(type='jeans', color='blue', size='medium', price=14.99), ClothingItem(type='jacket', color='black', size='x-large', price=19.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99), ClothingItem(type='shoes', color='white', size='12', price=24.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99)]