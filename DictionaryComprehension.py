"""
Dictionary Comprehension = Dictionary comprehension creates dictionary using an expressions can replace it
for loops and certain lambda function.
Dictionary = {key: expressions for (key, value) in iterable}
Dictionary = {key: expressions for (key, value) in iterable if conditional}
Dictionary = {key: (if/else) for (key, value) in iterable}
Dictionary = {key: function(value) for (key, value) in iterable}
"""
# from IPython.testing.tools import help_output_test
# from commctrl import HOTKEYF_ALT

cities_in_F = {"Patna" : 32, "UP" : 66, "Mumbai" : 78, "Bangalore" : 71, "Karnataka" : 94, "Ahmedabad" : 79}
cities_in_C = {key: round((value-32)*(5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {"Patna" : "Sunny", "Mumbai" : "Cloudy", "Delhi" : "Rainy", "Kashmir" : "Snowing"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "Sunny"}
print(sunny_weather)

cities = {"Patna" : 32, "UP" : 36, "Mumbai" : 118, "Bangalore" : 71, "Karnataka" : 94, "Ahmedabad" : 79}
desc_cities = {key: ("WARM" if value >= 40 else "Cold") for (key, value) in cities.items()}
print(desc_cities)

def check_temp(value):
    if value >= 60:
        return "HOT"
    elif 50>= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"Patna" : 32, "UP" : 36, "Mumbai" : 28, "Bangalore" : 71, "Karnataka" : 94, "Ahmedabad" : 79}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)