
# Day 4 - Cinema Ticket Pricing System
age = int(input("Enter age: "))
day = input("Enter day of the week: ").lower()
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

# Base ticket price
base_price = 500

# Set price by age using if / elif / else
if age < 5:
    category = "Child (Under 5)"
    discount = 100
    final_price = 0

elif age < 18:
    category = "Minor (5 - 17)"
    discount = 50
    final_price = base_price * 0.5

elif age >= 60:
    category = "Senior (60+)"
    discount = 30
    final_price = base_price * 0.7

else:
    category = "Adult"
    discount = 0
    final_price = base_price

# Extra discount for members on weekdays
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

if is_member and day in weekdays:
    final_price = final_price * 0.9
    discount += 10

# Nested if for popcorn offer
if final_price == 0:
    popcorn_offer = "No popcorn offer"
else:
    if is_member:
        popcorn_offer = "Large free popcorn"
    else:
        popcorn_offer = "Small free popcorn"

# Ternary expression
message = "Free entry" if final_price == 0 else "Enjoy the show!"

print("\n----- TICKET SUMMARY -----")
print("Category:", category)
print("Discount Applied:", str(discount) + "%")
print("Popcorn Offer:", popcorn_offer)
print("Final Price: Rs", final_price)
print("Message:", message)
