import os
import csv
import sqlite3

# Code that transfers a .csv file to a database
def transfer(filepath, curso):
    # Connect to SQLite database
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    #c.execute('INSERT INTO Instituicao (codigo, nome, ensinoSuperior) VALUES (?, ?, ?)',("1105", "FEUP", True))

    # Read data from CSV file
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            #print(row)
            #print("\n")
            ids = int(row['id'])
            codigo = row['codigo']
            nome = row['nome']
            media = row['media']
            opcao = int(row['opcao'])
            pi = float(row['pi'])
            ano12 = float(row['ano12'])
            ano1011 = float(row['ano1011'])

            # Insert data into table
            c.execute('INSERT INTO candidatura (id, codigo, nome, media, opcao, pi, ano12, ano1011, curso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (ids, codigo, nome, media, opcao, pi, ano12, ano1011, curso))

    # Commit changes and close connection
    conn.commit()
    conn.close()
    os.remove(filepath)