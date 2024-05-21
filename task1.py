import sys
import os
from pathlib import Path
import shutil

if len(sys.argv) < 2:
    print("Not enough parameters")
    exit(1)

#print(sys.argv)

source = sys.argv[1]
if len(sys.argv) == 3:
    destination = sys.argv[2]
else:
    destination = 'dist'

#print(source)
#print(destination)

def copy_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.copy(source, destination)

def inspect_directory(source):
    p = Path(source)
    try:
        for d in p.iterdir():
            if d.is_dir():
                inspect_directory(str(d))
            else:
                f = str(d).split('.')
                new_path = "{dist}/{ext}".format(dist = destination, ext = f[-1].lower())
                copy_files(str(d), new_path)

    except PermissionError:
        print(f"Permission denied for {p}")

if __name__ == "__main__":
    inspect_directory(source)
