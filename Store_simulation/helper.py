def display_products(product_dict):
    print("\n🛒 Product List:")
    for name, data in product_dict.items():
        print(f"- {name}: Rp{data['price']:,} (Stock: {data['stock']})")

def input_text(prompt):
    return input(prompt).strip()

def input_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("❌ Please enter a valid number.")
        return None