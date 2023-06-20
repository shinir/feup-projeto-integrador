import matplotlib.pyplot as plt


def plot_candidatos(conn, cursor, course_id_list, save_filename):
    # Create a new figure
    plt.figure()

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = "SELECT id, media, curso FROM candidatura WHERE curso = ?"
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        for row in cursor:
            x = row[0]
            y = float(row[1])

            x_values.append(x)
            y_values.append(y)

        # Plot the data for the current course
        plt.plot(x_values, y_values, label=f'Course ID: {course_id}')

    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Candidatos")
    plt.legend()
    plt.savefig(save_filename)
    plt.close()


def plot_colocados(conn, cursor, course_id_list, save_filename):
    # Create a new figure
    plt.figure()

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = "SELECT Candidatura.id, Candidatura.media, Candidatura.curso FROM Colocado JOIN Candidatura ON Colocado.nome = Candidatura.nome AND candidatura.curso = ?"
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        for row in cursor:
            x = row[0]
            y = float(row[1])

            x_values.append(x)
            y_values.append(y)

        # Plot the data for the current course
        plt.plot(x_values, y_values, label=f'Course ID: {course_id}')

    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Colocados")
    plt.legend()
    plt.savefig(save_filename)
    plt.close()
