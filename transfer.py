import os
import csv
import sqlite3

# Code that transfers a .csv file to a database
def transferCandidaturas(filepath, curso):
    # Connect to SQLite database
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    #c.execute('INSERT INTO Instituicao (codigo, nome, ensinoSuperior) VALUES (?, ?, ?)',("1105", "FEUP", True))

    # Read data from CSV file
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:

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



def transferCurso():
    # Connect to SQLite database
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    filePath = ""
    ano = input("Insert the year:")

    if ano == "2018":
        filePath = "csv/cna18_1f_resultados.csv"
    elif ano == "2019":
        filePath = "csv/cna19_1f_resultados.csv"
    elif ano == "2020":
        filePath = "csv/cna20_1f_resultados.csv"
    elif ano == "2021":
        filePath = "csv/cna21_1f_resultados.csv"
    elif ano == "2022":
        filePath = "csv/cna22_1f_resultados.csv"
    elif ano == "all":
        filePath = "csv/resultados.csv"

    #c.execute('INSERT INTO Instituicao (codigo, nome, ensinoSuperior) VALUES (?, ?, ?)',("1105", "FEUP", True))

    # Read data from CSV file
    with open(filePath, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        fieldnames = [fieldname.strip('\ufeff') for fieldname in csv_reader.fieldnames]
        csv_reader.fieldnames = fieldnames
        for row in csv_reader:

            # codInst;codCurso;Inst;Curso;Grau;Vagas;Colocados;Nota;Sobras
            ids = int(row['id'])
            codigo = row['codigo']
            nome = row['nome']
            vagas = int(row['vagas'])
            ano = int(row['ano'])
            instituicao = row['instituicao']

            try:
                # Insert data into table
                c.execute('INSERT INTO curso (codigo, nome, vagas, ano, instituicao) VALUES (?, ?, ?, ?, ?)',
                    (codigo, nome, vagas, ano, instituicao))
            except sqlite3.IntegrityError:
                # Handle constraint violation (e.g., print a message, log the error, etc.)
                print(f"Skipping INSERT due to constraint violation: {row}")

    # Commit changes and close connection
    conn.commit()
    conn.close()

transferCurso()