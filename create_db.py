import sqlite3

# Function to create the database and tables
def create_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Create table for guilds with added modrole field
    c.execute("""CREATE TABLE IF NOT EXISTS guilds (
                    guild_id INT PRIMARY KEY,
                    info_text TEXT,
                    category_1 TEXT,
                 )""")

    # Commit changes and close connection
    conn.commit()
    conn.close()

create_database()
