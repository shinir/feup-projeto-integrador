
from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sqlite3
import matplotlib.pyplot as plt

from graphs import plot

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database and retrieve data from the 'curso' table
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT c.instituicao, c.ano, c.nome, c.id FROM Curso c WHERE c.id IN (SELECT curso FROM Candidatura)")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('display.html', data=data)

@app.route('/generate_graphs', methods=['POST'])
def generate_graphs():
    selected_courses = request.form.getlist('courses')

    # Call the 'main' function to generate the graph for the selected courses
    graph_filename = main(selected_courses)
    return render_template('results.html', graph_url=graph_filename)

from flask import send_from_directory 
@app.route('/graphs/<filename>')
def serve_dynamic_image(filename):
    return send_from_directory('graphs', filename)

#@app.route('/results')
#def display_results():
    # Retrieve the 'graphs' parameter from the query string
 #   graph_filenames = request.args.get('graphs')

  #  if not graph_filenames:
        # Handle the case when no graphs were generated
   #     return render_template('no_results.html')

    # Split the filenames by comma
    #graph_filenames = graph_filenames.split(',')

    # Create a list of graph dictionaries
    #graphs = []
    #for graph_filename in graph_filenames:
     #   course_id = graph_filename.split('_')[1].split('.')[0]
      #  conn = sqlite3.connect('db/database.db')
       # cursor = conn.cursor()
        #cursor.execute("SELECT codigo, nome FROM Curso WHERE id = ?", (course_id,))
        #course = cursor.fetchone()

       # if course:
        #    course_code, course_name = course

         #   print(f"Course Code: {course_code}, Course Name: {course_name}")
            
          #  graph_info = {
           #     'title': f'Graph for {course_code} - {course_name}',
            #    'image': graph_filename
            #}
            #graphs.append(graph_info)

        # Close the database connection
        #cursor.close()
        #conn.close()

    # Render the 'results.html' template to display the generated graphs
    #return render_template('results.html', graphs=graphs)

def main(selected_courses):
    # Connect to the database and retrieve data for the selected courses
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()

    # Generate graphs for the selected courses
    plot(conn, cursor, selected_courses, 'graphs/all_courses.png')  # Call plot with the selected_courses list

    # Close the database connection
    cursor.close()
    conn.close()

    # Return generated graph
    return 'graphs/all_courses.png'


if __name__ == '__main__':
    app.run(debug =True)

