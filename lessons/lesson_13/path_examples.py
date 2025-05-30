import pathlib


curr_path = pathlib.Path(__file__)  # отримаємо шлях до поточного файла
curr_folder = pathlib.Path.cwd()  # шлях до поточної папки

parent_folder = curr_path.parent

new_unexisted_file = pathlib.Path(parent_folder, 'some_file.txt')


# print(curr_path)
# # print(curr_path.parent.parent, curr_path.parent.parent.exists())
# # print(new_unexisted_file, new_unexisted_file.exists())
#
# print(f'is file {curr_path}: {curr_path.is_file()}')
# print(f'is dir {curr_path}: {curr_path.is_dir()}')

# new_unexisted_file = pathlib.Path(parent_folder, 'asd', 'sdsds', 'some_file.txt')
new_unexisted_file = parent_folder / 'asd' / 'asdasd' / 'new_fiiiile.txt'

print(new_unexisted_file.name)
print(new_unexisted_file)

#
# new_dir = pathlib.Path.cwd() / 'new_folder_1'
# new_dir2 = pathlib.Path.cwd() / 'new_folder_1' / 'new_folder_2' / 'new_folder_3'
#
# new_dir.mkdir(exist_ok=True)
# new_dir2.mkdir(exist_ok=True, parents=True)
#
# import shutil
# shutil.rmtree(str(new_dir), ignore_errors=True)
#
# import os
#
# os.system('mkdir asd')
