import os

def get_files_info(working_directory, directory="."):
    # validate path to directory is inside working directory
    abs_path = os.path.abspath(working_directory)

    # construct full path from abs path and relative path
    target_dir = os.path.normpath(os.path.join(abs_path, directory))

    # check if target_dir falls within abs_path to working directory
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
        
