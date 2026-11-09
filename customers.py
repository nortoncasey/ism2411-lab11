# ISM2411 Lab 11 - Customer Dictionary & Lookup
# customers.py


# REFLECTION# 
# 1) When would I use .get() vs. bracket notation?
#    I would use bracket notation, like customer["name"], for keys that
#    every record must have, because if one is missing I want the program
#    to stop with a KeyError so I notice the bad data right away. I would
#    use .get() with a default for optional fields like phone or email,
#    where a missing value is normal and shouldn't crash a loop over
#    thousands of customers. My rule of thumb: brackets for required keys,
#    .get() for anything that might not be there.

# 2) What does the summary dictionary pattern remind me of from Excel?
#    Totaling sales by region with a loop reminds me of SUMIF or a
#    PivotTable in Excel, where you group rows by a category and add up
#    the amounts. The Python version is mor useful for large datasets
#    because it can work through millions of rows more then Excel's limit of
#     a million rows per sheet. It is also repeatable that can rerun the
#    same script on next month's data instead of rebuilding the table by
#    hand.
# 


# EXERCISE 1 - One customer

print("=== Exercise 1: One customer ===")

# A dictionary stores data as key: value pairs, like one row in a CRM
customer = {
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "tier": "gold",
    "ytd_spend": 1250.75,
}

# Key access: customer["key"] gives back the value stored under that key
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD spend:", customer["ytd_spend"])

# The whole dictionary at once
print(customer)
# EXERCISE 2 - Update and add

print("\n=== Exercise 2: Update and add ===")

# Assigning to a key that doesn't exist yet ADDS it
customer["phone"] = "813-555-0142"
print("After adding phone:", customer)

# Assigning to a key that already exists REPLACES its value
customer["tier"] = "platinum"
print("After updating tier:", customer)

# del removes a key and its value completely
del customer["email"]
print("After deleting email:", customer)

# EXERCISE 3 - Safe lookup
print("\n=== Exercise 3: Safe lookup ===")

# .get() returns the default when the key is missing, instead of crashing
email = customer.get("email", "no email on file")
print(".get() returned:", email)

# Bracket notation on a missing key raises a KeyError.
# try/except catches the error so the rest of the program still runs.
try:
    print(customer["email"])
except KeyError as error:
    print("Bracket notation raised a KeyError for", error)



# EXERCISE 4 - Iterate

print("\n=== Exercise 4: Iterate ===")

# .items() hands back each key AND its value together
for key, value in customer.items():
    print(f"{key}: {value}")

print("--- Without .items() ---")
for key in customer:
    print(key)

# Difference: looping over the dictionary by itself only gives you the
# KEYS (name, tier, ytd_spend, phone). .items() gives you each key and its
# value as a pair, so you can use both without having to look the value
# up again with customer[key].

 
# EXERCISE 5 - Lookup table

print("\n=== Exercise 5: Lookup table ===")

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
tier = customer["tier"]                       # "platinum" after Exercise 2
discount_rate = tier_discounts.get(tier, 0)   # 0 if the tier isn't listed
discount_amount = purchase * discount_rate
final_price = purchase - discount_amount

print("Tier:", tier)
print(f"Discount rate: {discount_rate:.0%}")  # :.0% shows 0.15 as 15%
print(f"Final price on a ${purchase} purchase: ${final_price:.2f}")



# EXERCISE 6 - List of dicts
 
print("\n=== Exercise 6: List of dicts ===")

customers = [
    {"name": "Brian Lee", "email": "brian@example.com", "tier": "bronze", "ytd_spend": 180.00},
    {"name": "Maria Garcia", "email": "maria@example.com", "tier": "silver", "ytd_spend": 640.50},
    {"name": "Jordan Smith", "email": "jordan@example.com", "tier": "gold", "ytd_spend": 1420.00},
    {"name": "Priya Patel", "email": "priya@example.com", "tier": "platinum", "ytd_spend": 3875.25},
]

purchase = 300
for person in customers:
    name = person["name"]
    tier = person["tier"]
    rate = tier_discounts.get(tier, 0)
    discount = purchase * rate
    print(f"{name} | tier: {tier} | discount on ${purchase}: ${discount:.2f}")



# EXERCISE 7 - Nested catalog

print("\n=== Exercise 7: Nested catalog ===")

# Each product name points to ANOTHER dictionary holding its details
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    stock = details["stock"]      # reach into the inner dictionary
    if stock < 20:
        print(f"LOW STOCK: {product} has only {stock} left")



# EXERCISE 8 - Sales by region

print("\n=== Exercise 8: Sales by region ===")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    # .get(region, 0) is the running total so far (0 the first time a
    # region shows up); add this sale's amount and store it back
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]

# sorted() on a dictionary returns its keys in alphabetical order
for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
