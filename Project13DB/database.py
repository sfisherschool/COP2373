import sqlite3
import matplotlib.pyplot as plt

# Database name
db_name = 'population_BL.db'

# Create a connection to the database
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create the population table
cursor.execute('''
CREATE TABLE IF NOT EXISTS population (
    city TEXT,
    year INTEGER,
    population INTEGER
)
''')

# List of cities and their initial population for 2023
cities = [
    ('Miami', 2023, 442241),
    ('Orlando', 2023, 309154),
    ('Tampa', 2023, 407599),
    ('Jacksonville', 2023, 949611),
    ('Tallahassee', 2023, 196169),
    ('St. Petersburg', 2023, 271842),
    ('Fort Lauderdale', 2023, 182760),
    ('Sarasota', 2023, 57014),
    ('Gainesville', 2023, 141085),
    ('Naples', 2023, 22139)
]

# Insert initial data into the population table
cursor.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', cities)
conn.commit()


# Function to simulate population growth
def simulate_population_growth():
    growth_rate = 0.02
    for city, year, population in cities:
        for i in range(1, 21):
            new_year = year + i
            new_population = int(population * ((1 + growth_rate) ** i))
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)',
                           (city, new_year, new_population))
    conn.commit()


simulate_population_growth()


# Function to show population growth for a city
def show_population_growth():
    city_options = [city[0] for city in cities]
    print("Choose a city from the following options:")
    for i, city in enumerate(city_options):
        print(f"{i + 1}. {city}")

    choice = int(input("Enter the number corresponding to the city: ")) - 1
    chosen_city = city_options[choice]

    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (chosen_city,))
    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth for {chosen_city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()


show_population_growth()

# Close the database connection
conn.close()
