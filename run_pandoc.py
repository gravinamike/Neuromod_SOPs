
import sys
import os
import shutil
from subprocess import call


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


if __name__ == '__main__':

    input_dir = sys.argv[1]############################################################# Generalize
    print input_dir

    pathiter = (os.path.join(root, filename)
        for root, _, filenames in os.walk(input_dir)
        for filename in filenames
        )

    for path in pathiter:

        head, tail = os.path.split(path)
        filename, extension = os.path.splitext(tail)
        if extension == '.txt' and not filename[:3] in ['SOP', 'WIP']:

            #os.chdir(head+'\\')

            call(['pandoc', path, '-o', filename+'.docx'])

###################################################################################### Exclude the Git repo directory. Make it include images
