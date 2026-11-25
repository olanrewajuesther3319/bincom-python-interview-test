
import random
import statistics
from collections import Counter

# 1. COLOUR DATA
colours = """
GREEN YELLOW GREEN BROWN BLUE PINK BLUE YELLOW ORANGE CREAM
ORANGE RED WHITE BLUE WHITE BLUE BLUE BLUE GREEN

ARSH BROWN GREEN BROWN BLUE BLUE BLEW PINK PINK ORANGE
ORANGE RED WHITE BLUE WHITE WHITE BLUE BLUE BLUE

GREEN YELLOW GREEN BROWN BLUE PINK RED YELLOW ORANGE RED
ORANGE RED BLUE BLUE WHITE BLUE BLUE WHITE WHITE

BLUE BLUE GREEN WHITE BLUE BROWN PINK YELLOW ORANGE CREAM
ORANGE RED WHITE BLUE WHITE BLUE BLUE BLUE GREEN

GREEN WHITE GREEN BROWN BLUE BLUE BLACK WHITE ORANGE RED
RED RED WHITE BLUE WHITE BLUE BLUE BLUE WHITE
""".split()

# 2. DATA CLEANING
cleaned_colours = []

for colour in colours:
    if colour == "BLEW":
        colour = "BLUE"
    cleaned_colours.append(colour)

# 3. COUNT COLOURS
frequency = Counter(cleaned_colours)

print("COLOUR FREQUENCIES")

for colour, count in sorted(frequency.items()):
    print(colour, ":", count)

# 4. MEAN
print("\nMean: Not applicable to categorical data.")

# 5. MOST WORN COLOUR (MODE)
print("\nMost worn colour:", frequency.most_common(1)[0][0])

# 6. MEDIAN
print("Median: Not applicable to categorical data.")

# 7. VARIANCE OF COLOUR FREQUENCIES
variance = statistics.pvariance(frequency.values())
print("Variance:", variance)

# 8. PROBABILITY OF RED
probability = frequency["RED"] / len(cleaned_colours)
print("Probability of RED:", probability)
print("Percentage:", probability * 100, "%")

# 9. SAVE TO POSTGRESQL
def save_to_postgresql():
    import psycopg2

    connection = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_username",
        password="your_password",
        port="5432"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colour_frequency (
            id SERIAL PRIMARY KEY,
            colour VARCHAR(50) UNIQUE,
            frequency INTEGER
        )
    """)

    for colour, count in frequency.items():
        cursor.execute("""
            INSERT INTO colour_frequency (colour, frequency)
            VALUES (%s, %s)
            ON CONFLICT (colour)
            DO UPDATE SET frequency = EXCLUDED.frequency
        """, (colour, count))

    connection.commit()
    cursor.close()
    connection.close()

    print("Data saved successfully!")


# 10. RECURSIVE SEARCH
def recursive_search(numbers, target, index=0):
    if index == len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return recursive_search(numbers, target, index + 1)


numbers = [10, 20, 30, 40, 50]

target = int(input("\nEnter a number to search: "))
result = recursive_search(numbers, target)

if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found.")

# 11. RANDOM 4-DIGIT BINARY NUMBER
binary_number = ""

for i in range(4):
    binary_number += str(random.randint(0, 1))

decimal_number = int(binary_number, 2)

print("\nBinary number:", binary_number)
print("Decimal number:", decimal_number)

# 12. SUM OF FIRST 50 FIBONACCI NUMBERS
a, b = 0, 1
total = 0

for i in range(50):
    total += a
    a, b = b, a + b

print("\nSum of first 50 Fibonacci numbers:", total)

