# task 1

import os

dir_name = os.path.join('--my_project', '--settings')
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    os.chdir('--my_project')
    os.makedirs('--mainapp')
    os.makedirs('--adminapp')
    os.makedirs('--authapp')