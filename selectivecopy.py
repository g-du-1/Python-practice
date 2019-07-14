#! python3
#  Walks through a folder tree
#  Searches for files with a certain extension
#  Copies from the location they are in
#  To a new folder

import os
import shutil


def selective_copy(source, destination, extension):

    # Makes new folder if it doesn't exist

    if not os.path.exists(destination):
        print('\nMaking directory: {}\n'.format(destination))
        os.makedirs(destination)

    # Copies all files with extension if they're not in the destination folder

    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(extension) and not os.path.isfile(os.path.join(destination, file)):
                print('Copying: {}'.format(file))
                shutil.copy2(os.path.join(root, file), destination)

    print()
    

if __name__ == '__main__':
    selective_copy('a', 'b', '.txt')
