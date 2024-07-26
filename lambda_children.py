children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}
]

criteria = lambda child: child["age"] > 3 and child["height"] > 100

eligible_children = [child for child in children if criteria(child)]

print("Expected Children for the fun park:", eligible_children)
