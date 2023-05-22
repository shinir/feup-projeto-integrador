import matplotlib.pyplot as plt
# import plotly
import csv

def plotCSV(filepath, sigla):
    for name, sig in zip(filepath,sigla):
        with open(name) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            # Read the header row
            header = next(reader)
            # Initialize lists to store data
            x = []
            y = []
            order = 0
            # Read each row of data and append to lists
            for row in reader:
                if int(row[4]) == 1:
                    order+=1
                    x.append(float(order))
                    y.append(float(row[3]))

        # Create the plot
        plt.plot(x,y,label=sig)
        plt.legend()
    plt.grid(True, "both")
    plt.xlabel("Número de Candidatos")
    plt.ylabel("Média de candidatura")
    plt.title('Candidatos em 1ª opção')
    plt.show()

def plot(conn, cursor):
    query = "SELECT id, media, curso FROM candidatura"
    cursor.execute(query)

    # Initialize dictionaries to store the grouped data
    data_dict = {}

    # Fetch and process the results
    for row in cursor:
        x = row[0]
        y = float(row[1])
        group = row[2]
        
        if group not in data_dict:
            data_dict[group] = {'x': [], 'y': []}
        
        data_dict[group]['x'].append(x)
        data_dict[group]['y'].append(y)

    # Create the plot
    for group, data in data_dict.items():
        plt.plot(data['x'], data['y'], label=group)

    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Candidatos em 1ª opção")
    plt.legend()
    plt.show()

    # Close the database connection
    cursor.close()
    conn.close()
