
from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    product_count = defaultdict(int)
    for order in orders:
        product_count[order] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
resultado = count_products(orders)
print(resultado)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})