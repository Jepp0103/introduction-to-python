# os_module.py


import os

if os.path.isdir('os_exercises'):
    pass
else:
    os.mkdir('os_exercises')

os.chdir('os_exercises')

for i in range(1, 4):
    t = input('Please write some code ')
    f = open(f'exercise_{i}.py', 'w')
    f.write(t)
    f.close()


for i in range(1, 4):
    print(len(set(open(f'exercise_{i}.py').read().split())))
