import os
from os import path

def rename_files_with_integers(directory):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if path.isfile(path.join(directory, f))]
    
    # Sort files to ensure consistent renaming order
    files.sort()
    
    i = 1
    new_names = []
    # Loop through files and rename them with integers
    for filename in files:
        if '.jpeg' in filename: 
            
            # Create new file name with integer
            new_name = f'{i}.jpeg'
            
            # Get full file paths
            old_file = path.join(directory, filename)
            new_file = path.join(directory, new_name)
            
            # Rename file
            if not path.exists(new_file):
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {new_name}")
                new_names += [new_name]
            else: 
                print(f"File {new_name} already exists")
                new_names += [filename]
                
            i += 1
        
    print(new_names)


# Use the current directory
current_directory = os.getcwd()

# Rename files in the current directory
rename_files_with_integers(current_directory)
