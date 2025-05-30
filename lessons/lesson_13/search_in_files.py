from constants import BASE_DIR
#
# for item_name in BASE_DIR.iterdir():
#     if item_name.is_file() and  item_name.suffix == '.py':
#         print(item_name)

import os
import pathlib


folder_to_search = pathlib.Path(BASE_DIR, 'tests', 'function_tests')

for item in os.walk(str(folder_to_search)):
    # path_to_folder, folders, files = item
    path_to_folder = item[0]


    #  якщо шлях о поточної папки починаеться з  BASE_DIR.venv то скіпай
    if path_to_folder.startswith(str(pathlib.Path(BASE_DIR, '.venv'))):
        continue

    if '__pycache__' in path_to_folder:
        continue

    folders = item[1]
    files = item[2]
    for file_name in files:
        if file_name.startswith('test_'):
            full_path = pathlib.Path(path_to_folder, file_name)
            print(full_path)