import matplotlib.pyplot as plt


def plot_candidatos(conn, cursor, course_id_list, save_filename):
    plt.figure(figsize=(7,7))
    ax= plt.subplot(111)
    # Iterate over the selected courses
    for course_id in course_id_list:
        query = """
        SELECT c.id, c.media, cu.nome, cu.ano, i.nome
        FROM Candidatura c
        INNER JOIN Curso cu ON c.curso = cu.id
        INNER JOIN Instituicao i ON i.codigo==cu.instituicao
        WHERE c.curso = ? AND c.opcao=1
        """
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        x=0
        for row in cursor:
            y = float(row[1])
            course_name = row[2]
            course_year= row[3]
            course_inst= row[4]
            x_values.append(x)
            x=x+1
            y_values.append(y)

        # Plot the data for the current course with the course name as the label
    
        ax.plot(x_values, y_values, label=course_inst+" - "+course_name + "-" + str(course_year))
    
    
    plt.xlabel("Número de candidatos")
    plt.ylabel("Média de candidatura")
    plt.title("Candidatos em 1ª opção")
    plt.legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(save_filename,bbox_inches='tight')
    plt.close()


def plot_colocados(conn, cursor, course_id_list, save_filename):
    plt.figure(figsize=(7,7))
    ax= plt.subplot(111)

    # Iterate over the selected courses
    for course_id in course_id_list:
        query = """
        SELECT c.id, c.media, cu.nome, cu.ano,i.nome
        FROM Candidatura c, Curso cu, Colocado co, Instituicao i
        WHERE c.curso = cu.id
		AND c.curso = co.curso
		AND co.nome=c.nome
        AND i.codigo==cu.instituicao
        AND c.curso = ?;
        """
        cursor.execute(query, (course_id,))

        # Initialize lists to store the x and y values
        x_values = []
        y_values = []

        # Fetch and process the results
        x=0
        for row in cursor:
            
            y = float(row[1])
            course_name = row[2]
            course_year= row[3] 
            course_inst= row[4]
            x_values.append(x)
            x=x+1
            y_values.append(y)

        # Plot the data for the current course with the course name as the label
    
        ax.plot(x_values, y_values, label=course_inst+" - "+course_name + "-" + str(course_year))
    plt.xlabel("Número de colocados")
    plt.ylabel("Média de candidatura")
    plt.title("Colocados")
    plt.legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(save_filename,bbox_inches='tight')
    plt.close()