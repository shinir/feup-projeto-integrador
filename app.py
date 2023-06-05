#from flask import Flask, render_template
#import sqlite3
#import matplotlib.pyplot as plt
#from graphs import plot

#app = Flask(__name__)

#@app.route('/')
#def index():
#    # Connect to the database
#    conn = sqlite3.connect('db/database.db')
#    cursor = conn.cursor()

    # Retrieve data from the database
#    cursor.execute("SELECT * from candidatura")
#    data = cursor.fetchall()

#    plot(conn, cursor)

    # Close the database connection
#    cursor.close()
#    conn.close()

    # Render the template and pass the data
#    return render_template('display.html', data=data)

#if __name__ == '__main__':
#    app.run()

from flask import Flask, render_template, request, redirect
import subprocess
import sqlite3
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database and retrieve data from the 'curso' table
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT c.instituicao, c.ano, c.nome FROM Curso c WHERE c.id IN (SELECT curso FROM Candidatura)")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('display.html', data=data)

@app.route('/generate_graphs', methods=['POST'])
def generate_graphs():
    selected_courses = request.form.getlist('courses')

    # Call the 'main' function to generate the graphs for the selected courses
    main(selected_courses)

    return redirect('/results')

@app.route('/results')
def display_results():
    # Render the 'results.html' template to display the generated graphs
    return render_template('results.html')

def main(selected_courses):
    # Connect to the database and retrieve data for the selected courses
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()

    # Initialize a list to store the generated graphs
    graphs = []

    # Generate graphs for each selected course
    for course_id in selected_courses:
        # Retrieve course information
        cursor.execute("SELECT codigo, nome FROM Curso WHERE id = ?", (course_id,))
        course = cursor.fetchone()

        if course:
            course_code, course_name = course

            # Generate graph based on course data
            # Example code: Generate a PNG file with a simple graph
            x = [1, 2, 3, 4, 5]
            y = [5, 4, 3, 2, 1]

            plt.plot(x, y)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(f'Graph for {course_code} - {course_name}')
            
            # Save the graph as a PNG file in the 'static' folder
            graph_filename = f'graphs/graph_{course_id}.png'
            plt.savefig(graph_filename)
            plt.close()

            # Create a dictionary to store the graph information
            graph_info = {
                'title': f'Graph for {course_code} - {course_name}',
                'image': graph_filename
            }

            # Add the graph to the list of generated graphs
            graphs.append(graph_info)

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the list of generated graphs
    return graphs


if __name__ == '__main__':
    app.run(debug =True)

