import csv

# Дані для запису у CSV-файл
data = [
    ['Name','has_kids', 'Age', 'phone','City'],
    ['John', 'yes', 30, '+38', 'New York'],
    ['Alice', 'yes', 25,'+38', 'Los Angeles'],
    ['Bob', 'no', 35, '+38', 'Chicago']
]

with open('output2.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

print(data)

header = data[0]
rows = data[1:]
print(f'headers: {header}')
print(f'rows: {rows}')
# rows = [dict(zip(header, row)) for row in rows]
final_rows = []
for row in rows:
    # dict(zip(header, row)) = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3]}
    final_rows.append(dict(zip(header, row)))


for row in final_rows:
    print(f'User: {row.get("Name")} is {row.get("Age")} years old')

print(final_rows)