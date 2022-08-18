# exercise 4
# i do not know how to do this yet :( sorry
import os

def split_file(file_name, split_size):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), split_size):
            with open(file_name + '-' + str(i), 'w') as f:
                f.writelines(lines[i:i+split_size])
            os.rename(file_name + '-' + str(i), file_name + '-' + str(i) + '.txt')
