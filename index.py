def greet(name):
    return f"Hello, {name}!"

def calculate_area(radius):
    return 3.14159 * radius ** 2

user_name = "World"
circle_radius = 5
greeting = greet(user_name)
area = calculate_area(circle_radius)
print(f"{greeting} Circle area: {area}")
