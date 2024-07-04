import csv

data = [
    ['Name', 'Age', 'City'],
    ['John Doe', '25', 'New York'],
    ['Jane Smith', '30', 'London'],
    ['Mike Johnson', '35', 'Paris']
]

filename = '/Users/lozingaro/Developer/MAST_learn/python/test/data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Test file '{filename}' created successfully.")
