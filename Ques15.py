import csv

# Data to be written to the CSV file
data = [
    [1, 2],
    [1, 2, 3]
]

# Write data to the CSV file
with open("Data.csv", "w", newline='') as fileobj:
    writerobj = csv.writer(fileobj)
    for row in data:
        writerobj.writerow(row)

# Verify if data is written correctly by reading the file
with open("Data.csv", "r") as fileobj:
    readerobj = csv.reader(fileobj)
    for row in readerobj:
        print(row)
