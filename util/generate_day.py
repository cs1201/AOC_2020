import sys
import os
import shutil
import fileinput

here = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.dirname(here)
blank_py_file = os.path.join(here, "day_X.py")
data_dir = os.path.join(target_dir, "data")

if len(sys.argv) < 2:
    print("No day number given")
    sys.exit()

# Create empty py file
day_number = sys.argv[1]
new_py_file = os.path.join(target_dir, f"day_{day_number}.py")
print(new_py_file)
shutil.copyfile(blank_py_file, new_py_file)
with fileinput.FileInput(new_py_file, inplace=True, backup='.bak')as py_file:
    for line in py_file:
        print(line.replace("day_X.txt", f"day_{day_number}.txt"), end='')
os.remove(f"day_{day_number}.py.bak")


# Create empty data .txt file
open(f"{data_dir}/day_{day_number}.txt", "a").close
