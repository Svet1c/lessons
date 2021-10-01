# task 3
import os
import shutil


if not os.path.exists('my project/templates'):
    os.mkdir('my project/templates')
curr_dir = ''
file_list = []
for root, dirs, files in os.walk("my project"):
    for file in files:
        if '.html' in file:
            file_list.append(os.path.join(root))

print(file_list)
os.chdir('my project/templates')
path_list = []
for path in file_list:
    path = path[path.find('templates\\') + len('templates\\'):]
    path_list.append(path)
    if not os.path.exists(path):
        os.makedirs(path)
os.chdir('..')
os.chdir('..')

for path in path_list:
    for root, dirs, files in os.walk(f"my project/{path}"):
        for file in files:
            if root == 'my project\\templates':
                break
            if '.html' in file:
                print(file)
                shutil.copy(os.path.join(root, file), f'my project/templates/{path}')
