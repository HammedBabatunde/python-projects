import os

path = '/home/dev_babs/Music/'

def rename_files():
    i = 0
    for file in os.listdir(path):
        file_dest = f'picture{i}.img'
        file_source = path + file
        file_dest = path + file_dest
        os.rename(file_source, file_dest)
        i += 1

rename_files()
