import matplotlib.pyplot as plt
import csv

# Open the CSV file
with open('csv/leic2022.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    # Read the header row
    header = next(reader)
    # Initialize lists to store data
    x = []
    y = []
    # Read each row of data and append to lists
    for row in reader:
        x.append(row[3])
        y.append(float(row[3]))

# Create the plot
plt.plot(x, y)
plt.xlabel("Number of candidates")
plt.ylabel("Media of candidates")
plt.title('Data Plot')
plt.show()
