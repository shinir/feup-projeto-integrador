import matplotlib.pyplot as plt


def plot(conn, cursor, course_id_list):
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
    plt.title("Candidatos em 1ª opção")
    plt.legend()
    plt.show()
