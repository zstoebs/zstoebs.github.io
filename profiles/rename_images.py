import os
from os import path

def rename_files_with_integers(directory):
    files = [f for f in os.listdir(directory) if path.isfile(path.join(directory, f)) and '.jpeg' in f]

    new_names = [f"{i}.jpeg" for i in range(1, len(files) + 1)]
    unmapped = set(files) - set(new_names)
    mapped = set(files) & set(new_names)
    mappable = set(new_names) - set(mapped)

    print('Files to be renamed:', unmapped)
    print('New names available:', mappable)

    for filename, new_name in zip(unmapped, mappable):

        old_file = path.join(directory, filename)
        new_file = path.join(directory, new_name)

        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

    print(new_names)

current_directory = os.getcwd()
rename_files_with_integers(current_directory)
