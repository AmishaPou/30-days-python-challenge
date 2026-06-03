# Day 3 – Mini Project: Personal Bio-Data Card

# Read full name and city (string)
full_name = input("Enter your full name: ")
city = input("Enter your city: ")

# Read age (int) and height (float)
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

# Create a boolean from a yes/no question
student_input = input("Are you a student? (yes/no): ").lower()
is_student = student_input == "yes"

# Read birth date and store in a tuple
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))
birth_date = (day, month, year)

# Read three hobbies and store in a list
hobbies = []
for i in range(1, 4):
    hobby = input(f"Enter hobby {i}: ")
    hobbies.append(hobby)

# Read three languages and store in a set
languages = set()
for i in range(1, 4):
    language = input(f"Enter language {i}: ")
    languages.add(language)

# Combine everything into a dictionary
profile = {
    "name": full_name,
    "city": city,
    "age": age,
    "height": height,
    "student": is_student,
    "birth_date": birth_date,
    "hobbies": hobbies,
    "languages": languages
}

# Print formatted bio-data card
print("          PERSONAL BIO-DATA CARD")
print("=" * 50)

print(f"Name        : {profile['name']}")
print(f"City        : {profile['city']}")
print(f"Age         : {profile['age']}")
print(f"Height      : {profile['height']} m")
print(f"Student     : {profile['student']}")
print(f"Birth Date  : {profile['birth_date']}")
print(f"Hobbies     : {profile['hobbies']}")
print(f"Languages   : {profile['languages']}")

print("\nAdditional Information")
print(f"First letter of name      : {full_name[0]}")
print(f"Number of hobbies         : {len(hobbies)}")
print(f"Number of unique languages: {len(languages)}")

print("\nData Types Verification")
print("-" * 50)
print(f"Name Type       : {type(full_name)}")
print(f"Age Type        : {type(age)}")
print(f"Height Type     : {type(height)}")
print(f"Student Type    : {type(is_student)}")
print(f"Birth Date Type : {type(birth_date)}")
print(f"Hobbies Type    : {type(hobbies)}")
print(f"Languages Type  : {type(languages)}")
print(f"Profile Type    : {type(profile)}")
