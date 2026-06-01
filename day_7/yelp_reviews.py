"""
Restaurant Attributes:
- capacity, size, location, menu, style, rating, hours, employees, orders, seating
- prices, customers, service quality, wait time, name, reviews, rewards program
- careers, nutrition, catering, pictures, suppliers, cleanliness, socials
- certifications, food quality

"""

class MenuItem:

    def __init__ (self, name, price, category, calories, ingredients):
        self.name = name
        self.price = price
        self.category = category
        self.calories = calories
        self.ingredients = ingredients

    def __str__ (self):
        return f"{self.name} | ${self.price:.2f} | {self.category} | {self.calories} calories | Allergens: {self.ingredients}"

class Restaurant:

    def __init__ (self, name, location, hours, style, capacity):
        self.name = name
        self.menu = []
        self.location = location
        self.hours = hours
        self.style = style
        self.capacity = capacity
        self.reviews = []
        self.prices = []
        self.contact = {}  # phone sumber, email

    def __str__ (self):
        return f"{self.name}, {self.style} Restaurant, Location: {self.location}, \
Hours: {self.hours}, Price Range: {self.calc_price_range()}, \
Menu: {len(self.menu)}\n \n{self.convert_menu_to_str()}"
    
    # Inputs: none
    # Processes: loop through menu items, find min and. max
    # Outputs: Min-Max
    def calc_price_range(self):
        if len(self.menu) == 0:
            return "No menu items"
        
        min_price = 99999999
        max_price = 0
        for menu_item in self.menu:
            if menu_item.price < min_price:
                min_price = menu_item.price
            if menu_item.price > max_price:
                max_price = menu_item.price
        return f"${min_price} - ${max_price}"
    
    def convert_menu_to_str(self):
        menu_str = ""
        for menu_item in self.menu:
            menu_str += f"{menu_item.name} | ${menu_item.price}\n"
        return menu_str
    

restaurant_1 = Restaurant("Wing Stop", "Orem", "11-11", "Fast Food", 4)
restaurant_2 = Restaurant("Blue Line Deli", "Provo", "11-11", "Grab and Go", 60)

menu_item_1 = MenuItem("Hot Wings", 8.99, "Entree", 800, "Eggs and Dairy")
menu_item_2 = MenuItem("Drumsticks", 7.99, "Entree", 850, "Eggs and Dairy")
menu_item_3 = MenuItem("Fries", 3.99, "Side", 270, "none")
menu_item_4 = MenuItem("Burrito", 11.99, "Entree", 900, "Dairy and Gluten")

restaurant_1.menu.append(menu_item_1)
restaurant_1.menu.append(menu_item_2)
restaurant_2.menu.append(menu_item_3)
restaurant_2.menu.append(menu_item_4)

print(restaurant_1)
print(restaurant_2)