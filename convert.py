print()
print('** UNIT CONVERTER **')
print()

conversions_available = [(1, 'inch', 'mm'), 
                         (2, 'mm', 'inch'),
                         (3, 'inch', 'cm'),
                         (4, 'cm', 'inch'),
                         (5, 'inch', 'm'),
                         (6, 'm', 'inch')
                         ]

print('Conversions available:')
print()

for conversion_number, from_unit, to_unit in conversions_available:
    print(f'{conversion_number}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter the number of the conversion to use --> ')
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> '))
print()

if conversion_number == 1:
    to_value = from_value * 25.4
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 2:
    to_value = from_value / 25.4
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 3:
    to_value = from_value * 2.54
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 4:
    to_value = from_value / 2.54 
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 5:
    to_value = from_value * 0.0254
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 6:
    to_value = from_value / 0.0254 
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    

     