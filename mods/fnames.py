import os

# Specify the directory path
directory_path = '.'  # Use current directory or provide the path you need

# Output text file
output_file = 'filenames.txt'

# Open the output file for writing
with open(output_file, 'w') as f:
    # Loop through all the files and directories in the specified path
    for filename in os.listdir(directory_path):
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(directory_path, filename)):
            # Write each filename to the text file
            f.write(filename + '\n')

print(f'All filenames have been written to {output_file}')
