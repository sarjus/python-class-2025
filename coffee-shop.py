# 0. Our starting dictionary
cafe_stock = {"Coffee": 100, "Sugar": 50, "Milk": 20}

# 1. dict.keys() -> Get all the item names
items = cafe_stock.keys()
print(f"Items in stock: {list(items)}")
# Result: ['Coffee', 'Sugar', 'Milk']

# 2. dict.values() -> Get all the quantities
quantities = cafe_stock.values()
print(f"Total quantities: {list(quantities)}")
# Result: [100, 50, 20]

# 3. dict.items() -> Get everything as pairs (perfect for loops)
for item, amount in cafe_stock.items():
    print(f"We have {amount} units of {item}")

# 4. dict.get(k, d) -> Check for an item safely
# 'Tea' isn't in our dict, so it returns 0 instead of crashing
tea_count = cafe_stock.get("Tea", 0)
print(f"Tea in stock: {tea_count}")

# 5. dict.pop(k) -> Remove an item and save its value
removed_value = cafe_stock.pop("Sugar")
print(f"Removed Sugar. It had {removed_value} units.")
# cafe_stock is now: {"Coffee": 100, "Milk": 20}

# 6. dict.update(d2) -> Add new items or change existing ones
new_delivery = {"Coffee": 150, "Cups": 500}
cafe_stock.update(new_delivery)
# Coffee is updated to 150, and Cups is added
print(f"Updated stock: {cafe_stock}")

# 7. dict.clear() -> Wipe the dictionary clean
cafe_stock.clear()
print(f"Stock after closing: {cafe_stock}")
# Result: {}