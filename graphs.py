import matplotlib.pyplot as plt


def plot_candidatos(conn, cursor, course_id_list, save_filename):
    plt.figure()

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = """
        SELECT c.id, c.media, cu.nome, cu.ano
        FROM Candidatura c
        INNER JOIN Curso cu ON c.curso = cu.id
        WHERE c.curso = ?
        """
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        for row in cursor:
            x = row[0]
            y = float(row[1])
            course_name = row[2]
            course_year= row[3]
            x_values.append(x)
            y_values.append(y)

        # Plot the data for the current course with the course name as the label
    
        plt.plot(x_values, y_values, label=course_name + "-" + str(course_year))

    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Candidatos em 1ª opção")
    plt.legend()
    plt.savefig(save_filename)
    plt.close()


def plot_colocados(conn, cursor, course_id_list, save_filename):
    plt.figure()

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = """
        SELECT c.id, c.media, cu.nome, cu.ano
        FROM Candidatura c
        INNER JOIN Curso cu ON c.curso = cu.id
        WHERE c.curso = ?
        """
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        for row in cursor:
            x = row[0]
            y = float(row[1])
            course_name = row[2]
            course_year= row[3]
            x_values.append(x)
            y_values.append(y)

        # Plot the data for the current course with the course name as the label
    
        plt.plot(x_values, y_values, label=course_name + "-" + str(course_year))
    plt.xlabel("Número de colocados")
    plt.ylabel("Média de candidatura")
    plt.title("Colocados")
    plt.legend()
    plt.savefig(save_filename)
    plt.close()
