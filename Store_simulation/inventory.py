products = {
    "Marlboro": {"price": 25000, "stock": 10},
    "Sampoerna": {"price": 23000, "stock": 15},
    "Djarum": {"price": 20000, "stock": 20}
}

def get_all_products():
    """Return the product list."""
    return products

def buy_product(name, quantity):
    """Process a product purchase."""
    if name not in products:
        return False, "Product not found."
    if quantity <= 0:
        return False, "Invalid quantity."
    if products[name]["stock"] < quantity:
        return False, "Not enough stock."

    total_price = quantity * products[name]["price"]
    products[name]["stock"] -= quantity
    return True, total_price

def restock_product(name, quantity):
    """Add stock to existing or new product."""
    if name not in products:
        products[name] = {"price": 0, "stock": 0}
    products[name]["stock"] += quantity

def update_price(name, new_price):
    """Update product price."""
    if name not in products:
        return False
    products[name]["price"] = new_price
    return True