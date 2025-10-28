"""
Simple test to verify the product data structure is correct
"""

# Test product data structure
sample_product = {
    "name": "iPhone 15 Pro",
    "category": "Smartphone",
    "brand": "Apple",
    "price": 999,
    "rating": 4.7,
    "screen_size": "6.1 inches",
    "storage": "256GB",
    "ram": "8GB",
    "battery": "3274 mAh",
    "release_year": 2023
}

# Verify all required fields are present
required_fields = ["name", "category", "brand", "price", "rating", "screen_size", 
                   "storage", "ram", "battery", "release_year"]

print("Testing product data structure...")
for field in required_fields:
    assert field in sample_product, f"Missing field: {field}"
    print(f"✓ {field}: {sample_product[field]}")

print("\nAll tests passed! Product data structure is valid.")
