import sys

# Conversion factors
conversion_factors = {
    ## From inch ##
    'inch_to_feet': 1 / 12,
    'inch_to_mm': 25.4, 
    'inch_to_cm': 2.54,
    'inch_to_dm': 0.254,
    'inch_to_m': 0.0254,
    'inch_to_km': 0.0000254,
    
    ## From feet ##
    'feet_to_inch': 12,
    'feet_to_mm': 304.8,
    'feet_to_cm': 30.48,
    'feet_to_dm': 3.048,
    'feet_to_m': 0.3048,
    'feet_to_km': 0.0003048,

    ## From mm ##
    'mm_to_inch': 1 / 25.4,
    'mm_to_feet': 1 / 304.8,
    'mm_to_cm': 1 / 10, 
    'mm_to_dm': 1 / 100,
    'mm_to_m': 1 / 1000,
    'mm_to_km': 1 / 1000000,

    ## From cm ##
    'cm_to_inch': 1 / 2.54,
    'cm_to_feet': 1 / 30.48,
    'cm_to_mm': 10, 
    'cm_to_dm': 1 / 10,
    'cm_to_m': 1 / 100,
    'cm_to_km': 1 / 100000,

    ## From dm ##
    'dm_to_inch': 3.937,
    'dm_to_feet': 1 / 3.048,
    'dm_to_mm': 100, 
    'dm_to_cm': 10,
    'dm_to_m': 1 / 10,
    'dm_to_km': 1 / 100000,

    ## From m ##
    'm_to_inch': 39.37,
    'm_to_feet': 3.281,
    'm_to_mm': 1000, 
    'm_to_cm': 100,
    'm_to_dm': 10,
    'm_to_km': 1 / 1000,
    
    ## From km ##
    'km_to_inch': 39370.1,
    'km_to_feet': 3281,
    'km_to_mm': 1000000,
    'km_to_cm': 100000,
    'km_to_dm': 10000,
    'km_to_m': 1000,

    ## From Pints ##
    'pints_to_quarts': 1 / 2,
    'pints_to_cups': 2.402,
    'pints_to_ml': 568.3,
    'pints_to_dl': 5.683,
    'pints_to_l': 1 / 1.76,

    ## From Quarts ##
    'quarts_to_pints': 2,
    'quarts_to_cups': 4,
    'quarts_to_ml': 946.4,
    'quarts_to_dl': 9.464,
    'quarts_to_l': 1.137,

    ## From Cups ##
    'cups_to_pints': 1 / 2,
    'cups_to_quarts': 1 / 4,
    'cups_to_ml': 236.6,
    'cups_to_dl': 2.366,
    'cups_to_l': 1 / 4.227,

    ## From ml ##
    'ml_to_pints': 1 / 568.3,
    'ml_to_quarts': 1 / 946.4,
    'ml_to_cups': 1 / 236.6,
    'ml_to_dl': 1 / 100,
    'ml_to_l': 1 / 1000,

    ## From dl ##
    'dl_to_pints': 1 / 4.732,
    'dl_to_quarts': 1 / 9.464,
    'dl_to_cups': 1 / 2.366,
    'dl_to_ml': 100,
    'dl_to_l': 1 / 10,

    ## From L ##
    'l_to_pints': 2.113,
    'l_to_quarts': 1.057,
    'l_to_cups': 4.227,
    'l_to_ml': 1000,
    'l_to_dl': 10,
}

# Unit abbreviations and their meanings for distances
distance_menu = {
    'inch': 'Inches',
    'feet': 'Feet',
    'mm': 'Millimeters',
    'cm': 'Centimeters',
    'dm': 'Decimeters',
    'm': 'Meters',
    'km': 'Kilometers',
}

# Unit abbreviations and their meanings for distances
distance_menu = {
    'inch': 'Inches',
    'feet': 'Feet',
    'mm': 'Millimeters',
    'cm': 'Centimeters',
    'dm': 'Decimeters',
    'm': 'Meters',
    'km': 'Kilometers',
}

# Unit abbreviations and their meanings for volumes
volume_menu = {
    'pints': 'Pints',
    'quarts': 'Quarts',
    'cups': 'Cups',
    'ml': 'Milliliters',
    'dl': 'Deciliters',
    'l': 'Liters',
}

# Display the distance menu
print("------- Distances -------")
for abbreviation, meaning in distance_menu.items():
    print(f"{abbreviation} - {meaning}")

# Display the volume menu
print("------- Volumes -------")
for abbreviation, meaning in volume_menu.items():
    print(f"{abbreviation} - {meaning}")

# Read the unit abbreviations from the user
unit_from = input("Enter the unit abbreviation to convert from: ")
unit_to = input("Enter the unit abbreviation to convert to: ")

# Check if the unit abbreviations are valid for distances or volumes
if unit_from not in distance_menu and unit_from not in volume_menu:
    print("Invalid unit abbreviation for conversion.")
    sys.exit()

if unit_to not in distance_menu and unit_to not in volume_menu:
    print("Invalid unit abbreviation for conversion.")
    sys.exit()

# Generate the conversion key based on the units
conversion_key = f"{unit_from}_to_{unit_to}"

# Check if the conversion key exists in the conversion factors dictionary
if conversion_key not in conversion_factors:
    print("Invalid conversion.")
    sys.exit()

# Read the value to be converted from user input
value = float(input("Enter the value to be converted: "))

# Perform the conversion based on the user's choice
result = value * conversion_factors[conversion_key]

# Determine the appropriate unit meaning based on distance or volume
if unit_from in distance_menu and unit_to in distance_menu:
    unit_from_meaning = distance_menu[unit_from]
    unit_to_meaning = distance_menu[unit_to]
elif unit_from in volume_menu and unit_to in volume_menu:
    unit_from_meaning = volume_menu[unit_from]
    unit_to_meaning = volume_menu[unit_to]

print(f"{value} {unit_from_meaning} is equal to {result} {unit_to_meaning}.")