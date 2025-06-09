import csv
from constants import LESSON_15_FOLDER

data = []
with open(LESSON_15_FOLDER / 'test_file.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        row_without_empty_values = [k for k in row if len(k) > 0]  # позбутись порожніх комірок
        data.append(row_without_empty_values)
print(*data, sep='\n')

with open(LESSON_15_FOLDER / 'new_test_file.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';')  # delimiter - роздільник між комірками
    writer.writerows(data[:2])