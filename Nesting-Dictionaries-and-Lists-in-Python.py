capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_Log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a List
travel_Log2 = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 18}
]

print(travel_Log)
print(travel_Log2)