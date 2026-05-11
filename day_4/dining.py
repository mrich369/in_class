# ============================================================
# Pattern Drill A: BYU Campus Dining
# ============================================================
# The data is already loaded — your job is to write the loops.
# Complete each TODO using a for loop.
# ============================================================

# --- DATA (do not modify) -----------------------------------
restaurants = ["Cupbop", "Costa Vida", "Chick-fil-A", "Subway",
               "Taco Bell", "MOD Pizza", "Panda Express"]
ratings     = [4.5, 4.2, 4.8, 3.1, 3.6, 4.0, 3.9]
prices      = [11.50, 9.75, 8.99, 7.25, 6.99, 10.50, 8.75]
# ------------------------------------------------------------


# TODO 1 — Accumulator
# Calculate the average rating across all restaurants.
# Hint: sum all ratings, then divide by the count.

ratings_sum = 0
for rate in ratings:
    ratings_sum += rate
avg_rating = ratings_sum / len(ratings)

print(f"Average rating: {avg_rating:.2f}")  # replace ___ with your variable


# TODO 2 — Filter
# Build a list of restaurants rated 4.0 or higher.
# Hint: loop through the indices so you can check ratings[i]
#       and grab restaurants[i].

top_restaurants = []
for i in range(len(ratings)):
    if ratings[i] >= 4.0:
        top_restaurants.append(restaurants[i])

print(f"Top-rated (4.0+): {top_restaurants}")  # replace ___ with your list


# TODO 3 — Search
# Check whether "Cupbop" is in the restaurant list.
# Use a boolean flag — do NOT use the `in` operator.
# Hint: start with found = False, flip it inside the loop.

found = False
for restaurant in restaurants:
    if restaurant == "Cupbop":
        found = True

"""
found = False
for i in range(len(restaurants)):
    if restaurants[i] == "Cupbop":
        found = True
"""

print(f"Cupbop found: {found}")  # replace ___ with your flag


# TODO 4 — Challenge (combine two patterns)
# Which restaurant has the best rating-to-price ratio?
# (rating / price = value score)
# Hint: you need a loop that tracks the best ratio AND
#       which restaurant it belongs to.

best_value_restaurant = ""
best_value = 0
for i in range(len(restaurants)):
    restaurant_value = ratings[i] / prices[i]
    if restaurant_value > best_value:
        best_value_restaurant = restaurants[i]
        best_value = restaurant_value

print(f"Best value: {best_value_restaurant} at {best_value:.2f}")  # replace ___ with the restaurant name