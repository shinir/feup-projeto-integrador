import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS Candidatura
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER,
              email TEXT)''')

# Read data from CSV file
with open('csv/leic2022.csv') as csv_file:
    print(csv_file)
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print("\n")
        print(row)
        print("\n")
        ids = int(row['identifier'])
        codigo = row['codigo']
        nome = row['nome']
        media = row['media']
        opcao = int(row['opcao'])
        pi = float(row['pi'])
        ano12 = float(row['ano12'])
        ano1011 = float(row['ano1011'])

        # Insert data into table
        c.execute("INSERT INTO Candidatura  (id, codigo, nome, media, opcao, pi, ano12, ano1011) VALUES (?, ?, ?)",
                  (ids, codigo, nome, media, opcao, pi, ano12, ano1011))

# Commit changes and close connection
conn.commit()
conn.close()
