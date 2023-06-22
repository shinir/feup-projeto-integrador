
from flask import Flask, render_template, request, redirect,current_app
import subprocess
import sqlite3
import matplotlib.pyplot as plt
from graphs import plot_candidatos
from graphs import plot_colocados

app = Flask(__name__)

app.config['MY_GLOBAL_VARIABLE'] = 0


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/candidatos')
def candidatos():
    # Connect to the database and retrieve data from the 'curso' table
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT c.instituicao, c.ano, c.nome, c.id ,i.nome FROM Curso c, Instituicao i WHERE c.id IN (SELECT curso FROM Candidatura) AND i.codigo==c.instituicao order by c.instituicao, c.nome,c.ano")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('display_candidatos.html', data=data)


@app.route('/candidatos_graph', methods=['POST'])
def candidatos_graph():    
    selected_courses = request.form.getlist('courses')

    # Call the 'main' function to generate the graph for the selected courses
    graph_filename = candidatos_plot(selected_courses)
    return render_template('results.html', graph_url=graph_filename)

#
@app.route('/colocados')
def colocados():
    # Connect to the database and retrieve data from the 'curso' table
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT c.instituicao, c.ano, c.nome, c.id ,i.nome FROM Curso c, Instituicao i WHERE c.id IN (SELECT curso FROM Candidatura) AND i.codigo==c.instituicao order by c.instituicao, c.nome,c.ano")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('display_colocados.html', data=data)


@app.route('/colocados_graph', methods=['POST'])
def colocados_graph():    
    selected_courses = request.form.getlist('courses')

    # Call the 'main' function to generate the graph for the selected courses
    graph_filename = colocados_plot(selected_courses)
    return render_template('results.html', graph_url=graph_filename)

#


from flask import send_from_directory 
@app.route('/graphs/<filename>')
def serve_dynamic_image(filename):
    return send_from_directory('graphs', filename)



def candidatos_plot(selected_courses):
   # Connect to the database and retrieve data for the selected courses
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    my_variable = current_app.config['MY_GLOBAL_VARIABLE']
    if(app.config['MY_GLOBAL_VARIABLE']==10):
        app.config['MY_GLOBAL_VARIABLE'] =app.config['MY_GLOBAL_VARIABLE'] +1
    else:
        app.config['MY_GLOBAL_VARIABLE'] =app.config['MY_GLOBAL_VARIABLE'] +1
    
    # Generate graphs for the selected courses
    plot_candidatos(conn, cursor, selected_courses, 'graphs/all_courses'+str(my_variable)+'.png')  # Call plot with the selected_courses list

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the list of generated graphs
    return 'graphs/all_courses'+str(my_variable)+'.png'

def colocados_plot(selected_courses):
    # Connect to the database and retrieve data for the selected courses
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    my_variable = current_app.config['MY_GLOBAL_VARIABLE']
    if(app.config['MY_GLOBAL_VARIABLE']==10):
        app.config['MY_GLOBAL_VARIABLE']=0
    else:
        app.config['MY_GLOBAL_VARIABLE'] =app.config['MY_GLOBAL_VARIABLE'] +1
    
    # Generate graphs for the selected courses
    plot_colocados(conn, cursor, selected_courses, 'graphs/all_courses'+str(my_variable)+'.png')  # Call plot with the selected_courses list

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the list of generated graphs
    return 'graphs/all_courses'+str(my_variable)+'.png'


if __name__ == '__main__':
    app.run(debug =True)

