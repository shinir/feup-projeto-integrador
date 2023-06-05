from flask import Flask, render_template
import sqlite3
import matplotlib.pyplot as plt
from graphs import plot

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute("SELECT * from candidatura")
    data = cursor.fetchall()

    #plot(conn, cursor)

    # Close the database connection
    cursor.close()
    conn.close()

    # Render the template and pass the data
    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
