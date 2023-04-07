import csv
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data1 = read_data('leic2022.csv')
    data2 = read_data('isep2022.csv')
    graph = create_graph(data1, data2)
    return render_template('display.html', graph=graph)

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def create_graph(data1, data2):
    x1 = [row[0] for row in data1[1:]]
    y1 = [float(row[4]) for row in data1[1:]]
    x2 = [row[0] for row in data2[1:]]
    y2 = [float(row[4]) for row in data2[1:]]
    plt.plot(x1, y1, label='LEIC')
    #plt.plot(x2, y2, label='ISEP')
    plt.title('Comparison of Candidates per Faculty')
    plt.xlabel('Number of candidates')
    plt.ylabel('Media')
    plt.legend()
    graph = plt.gcf()
    return graph

if __name__ == '__main__':
    app.run(debug=True)