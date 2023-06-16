import matplotlib.pyplot as plt


def plot(conn, cursor, course_id_list, save_filename):
    # Create a new figure
    plt.figure()

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = """
        SELECT c.id, c.media, cu.nome
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

            x_values.append(x)
            y_values.append(y)

        # Plot the data for the current course with the course name as the label
        plt.plot(x_values, y_values, label=course_name)

    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Candidatos em 1ª opção")
    plt.legend()
    plt.savefig(save_filename)
    plt.close()